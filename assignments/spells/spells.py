from datetime import datetime
import zipfile
from pathlib import Path


def mentions(book, text):
    output = ''
    # book_txt in the entire book and text in the spell or potion input from the main()
    try:
        book_txt = open(f'Harry Potter {book}.csv').read().split('\n')
    except:
        output = ('Book not found!\n')
        return output
    apperances = 0
    line_number = 0
    sorted_dict = {}

    for i in book_txt:
        line_number += 1
        if text in i:
            apperances += 1

            all_words_in_line = i.split(';')
            character_name = all_words_in_line[0].strip()

            if character_name not in sorted_dict:
                sorted_dict[character_name] = [line_number]
            else:
                sorted_dict[character_name].append(line_number)
    if apperances == 0:
        print(f'No apperances of {text} in book Harry Potter {book}.csv')
    else:
        print(f'{apperances} apperances of {text} in book Harry Potter {book}.csv')

    for key, value in sorted_dict.items():
        output += (f'\n{key} on line(s) {value}\n'.replace('[', '').replace(']', ''))
        character_details = character(key.capitalize())
        if character_details is None:
            continue
        output += str(character_details) + '\n'

    return output


def character(name):
    zipfile_ = zipfile.ZipFile(Path("HarryPotter.zip"))
    zipfile_.extractall()
    zipfile_.close()

    output = ''
    book_txt = open('Characters.csv').read().split('\n')

    for i in book_txt:
        if name in i:
            line_lst = i.split(';')
            if name in line_lst[1]:
                fullname = line_lst[1]
                house = line_lst[4]
                age = calculate_age((line_lst[13].strip().replace(", "," ")), (line_lst[14].strip().replace(", "," ")))
                if age == 1000000:
                    output = f'{fullname}\n{house}\n{name} is alive and kicking.'
                elif age == 200000:
                    output = f'{fullname}\n{house}\n{name} died.'
                elif line_lst[14] == '':
                    output = f'{fullname}\n{house}\n{name} is today {age} years old.'
                elif 0<age<100:
                    output = f'{fullname}\n{house}\n{name} died at age {age}'

                return output


def calculate_age(birth, death=''):
    if birth and death:
        try:
            death_date = datetime.strptime(death, '%d %B %Y').date()
        except ValueError:
            try:
                death_date = datetime.strptime(death, '%d %B, %Y').date()
            except ValueError:
                return 200000  # died
        try:
            birth_date = datetime.strptime(birth, '%d %B %Y').date()
        except ValueError:
            try:
                birth_date = datetime.strptime(birth, '%d %B, %Y').date()
            except ValueError:
                return 200000  # died

        age = (death_date - birth_date).days // 365
        return age  # died at

    if birth and not death:
        try:
            birth_date = datetime.strptime(birth, '%d %B %Y').date()
        except ValueError:
            try:
                birth_date = datetime.strptime(birth, '%d %B, %Y').date()
            except ValueError:
                return 1000000  # alive and kicking

        age = (datetime.now().date() - birth_date).days // 365
        return age  # age


def spell(text):
    zipfile_ = zipfile.ZipFile(Path("HarryPotter.zip"))
    zipfile_.extractall()
    zipfile_.close()
    txt = open('Spells.csv').read().split('\n')

    output = ''
    overview = {}
    for i in txt:
        if text in i:
            lst = i.split(';')
            if text in lst[0] or text in lst[1]:
                overview['Name:'] = lst[0]
                overview['Incantation:'] = lst[1]
                overview['Type:'] = lst[2]
                overview['Effect:'] = lst[3]
                overview['Light:'] = lst[4]
    for key, value in overview.items():
        output += f'{key} {value}\n'
    return output.strip()


def potion(text):
    zipfile_ = zipfile.ZipFile(Path("HarryPotter.zip"))
    zipfile_.extractall()
    zipfile_.close()
    txt = open('Potions.csv').read().split('\n')

    output = ''
    overview = {}
    for i in txt:
        if text in i:
            lst = i.split(';')
            if text in lst[0]:
                overview['Name:'] = lst[0]
                overview['Known ingredients:'] = lst[1]
                overview['Effect:'] = lst[2]
                overview['Characteristics:'] = lst[3]
                overview['Difficulty level:'] = lst[4]
    for key, value in overview.items():
        output += f'{key} {value}\n'
    return output.strip()


def main():
    # extract the zip file
    zipfile_ = zipfile.ZipFile(Path("HarryPotter.zip"))
    zipfile_.extractall()
    zipfile_.close()

    # input
    book_number = input()
    spell_potion = input().strip()

    # dictionary output
    mentions_details = mentions(book_number, spell_potion)
    print(mentions_details)

    spell_txt = open('Spells.csv').read()
    potion_txt = open('Potions.csv').read()
    if spell_potion in spell_txt:
        print(f'SPELL {spell_potion.strip()}')
        spell_output = spell(spell_potion)
        print(spell_output.strip())
    elif spell_potion in potion_txt:
        print(f'POTION {spell_potion}')
        potion_output = potion(spell_potion)
        print(potion_output.strip())
    else:
        print(f'{spell_potion.strip()} it is neither a spell nor a potion')


if __name__ == '__main__':
    main()
