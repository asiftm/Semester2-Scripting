from _datetime import datetime


def character(name):
    output = ''
    fullname = ''
    house = ''
    age = ''
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
                elif 0 < age < 100:
                    output = f'{fullname}\n{house}\n{name} died at age {age}'

                return output


def calculate_age(birth, death=''):
    if birth and death:
        try:
            death_date = datetime.strptime(death, '%d %B %Y').date()
            death_year = death_date.strftime("%Y")
            death_month = death_date.strftime("%B")
            death_day = death_date.strftime("%d")
        except ValueError:
            try:
                death_date = datetime.strptime(death, '%d %B, %Y').date()
                death_year = death_date.strftime("%Y")
                death_month = death_date.strftime("%B")
                death_day = death_date.strftime("%d")
            except ValueError:
                return 200000  # died
        try:
            birth_date = datetime.strptime(birth, '%d %B %Y').date()
            birth_year = birth_date.strftime("%Y")
            birth_month = birth_date.strftime("%B")
            birth_day = birth_date.strftime("%d")
        except ValueError:
            try:
                birth_date = datetime.strptime(birth, '%d %B, %Y').date()
                birth_year = birth_date.strftime("%Y")
                birth_month = birth_date.strftime("%B")
                birth_day = birth_date.strftime("%d")
            except ValueError:
                return 200000  # died

        age = int(death_year) - int(birth_year)

        if (death_month, death_day) > (birth_month, birth_day):
            age = age - 1

        return age  # died at

    if birth and not death:
        try:
            birth_date = datetime.strptime(birth, '%d %B %Y').date()
            birth_year = birth_date.strftime("%Y")
            birth_month = birth_date.strftime("%B")
            birth_day = birth_date.strftime("%d")
        except ValueError:
            try:
                birth_date = datetime.strptime(birth, '%d %B, %Y').date()
                birth_year = birth_date.strftime("%Y")
                birth_month = birth_date.strftime("%B")
                birth_day = birth_date.strftime("%d")
            except ValueError:
                return 1000000  # alive and kicking

        current_year = datetime.now().strftime("%Y")
        current_month = datetime.now().strftime("%B")
        current_day = datetime.now().strftime("%d")

        age = int(current_year) - int(birth_year)

        if (current_month, current_day) < (birth_month, birth_day):
            age = age - 1

        return age


print(character('Ronald Bilius Weasley'))
# print(calculate_age('23 April 1980'))