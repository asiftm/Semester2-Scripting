from art import *


def forbidden(plate):
    forbidden_letter_combinations = 'AAP AAS AEL ALA ANE ASS BEB BIT BOM BOY BSP BUB BWP BYT CAP CDF CDH CDV CON CSP CUB CUL CUT CVP DCD DIK DOM FDF FOK FOL FOU FUC FUK GAT GAY GEK GOD HIV HOL JEK KAK KKQ KUL KUT LAF LDD LSP LUL MAS MCC MDP MOR MOU MST NIC NIK NIQ NVA PDB PDO PET PFF PIK PIN PIP PIS PJU PKK POT PRL PSB PSC PSL PTB PUE PUT PVV PYK PYN PYP PYS ROM SEX SOA SOT SPA SUL TAK TET TIT TUE VCD VIH VLD VMO VNV ZAC ZAK ZOT'
    forbidden_list = forbidden_letter_combinations.split(' ')
    condition = False
    for i in forbidden_list:
        if i in plate:
            condition = True
            break
        else:
            condition = False
    return (condition)


def check(plate):
    # forbidden
    forbidden_letter_combinations = 'AAP AAS AEL ALA ANE ASS BEB BIT BOM BOY BSP BUB BWP BYT CAP CDF CDH CDV CON CSP CUB CUL CUT CVP DCD DIK DOM FDF FOK FOL FOU FUC FUK GAT GAY GEK GOD HIV HOL JEK KAK KKQ KUL KUT LAF LDD LSP LUL MAS MCC MDP MOR MOU MST NIC NIK NIQ NVA PDB PDO PET PFF PIK PIN PIP PIS PJU PKK POT PRL PSB PSC PSL PTB PUE PUT PVV PYK PYN PYP PYS ROM SEX SOA SOT SPA SUL TAK TET TIT TUE VCD VIH VLD VMO VNV ZAC ZAK ZOT'
    forbidden_list = forbidden_letter_combinations.split(' ')
    forbidden_bool = forbidden(plate)
    if forbidden_bool == True:
        for i in forbidden_list:
            if i in plate:
                return (f'forbidden plate - {i}')

    # special
    if ('1' <= plate <= '9') and plate.isdigit():
        return (f'special plate - king and queen')
    elif ('10' <= plate <= '09') and plate.isdigit():
        return (f'special plate - royal')
    elif 'A-1' <= plate <= 'A-999':
        return (f'special plate - official')
    elif 'CD-AA111' <= plate <= 'CD-ZZ999':
        return ('special plate - diplomat')
    elif 'G-LAA-111' <= plate <= 'G-LZZ-999':
        return ('special plate - agriculture')
    elif 'M-AAA-000' <= plate <= 'M-ZZZ-999':
        return ('special plate - motorcycle')
    elif 'O-AAA-111' <= plate <= 'O-ZZZ-999':
        return ('special plate - oldtimer')
    elif 'Q-AAA-000' <= plate <= 'Q-ZZZ-999':
        return ('special plate - trailer')
    elif 'T-XAA-000' <= plate <= 'T-XZZ-999':
        return ('special plate - taxi')
    elif 'Y-AAA-000' <= plate <= 'Y-ZZZ-999':
        return ('special plate - test')
    # standard
    elif '1-AAA-001' <= plate <= '7-ZZZ-999':
        return ('standard plate - 2010-now')
    elif 'AAA-001' <= plate <= 'ZZZ-999':
        return ('standard plate - 1973-2008')
    elif 'A.001.A' <= plate <= 'Z.999.Z':
        return ('standard plate - 1971-1973')
    elif 'AA.001' <= plate <= 'ZZ.999':
        return ('standard plate - 1962-1971')
    elif '001-AAA' <= plate <= '999-CFQ':
        return ('standard plate - 2008-2010')


def nato(input_licence):
    nato_dict = {'A': 'Alfa', 'B': 'Beta', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxstrot', 'G': 'Golf',
                 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November',
                 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform',
                 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-Ray', 'Y': 'Yankee', 'Z': 'Zulu', '0': 'Zero', '1': 'One',
                 '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight',
                 '9': 'Nine'}
    nato_text = ''
    input_licence = input_licence.upper()
    for i in input_licence:
        for j in nato_dict.keys():
            if i == j:
                nato_text += nato_dict[i] + ' '
    return (nato_text.upper())


def ascii(input_licence):
    ascii_format = text2art(input_licence)
    return (ascii_format)


def morse(input_licence):
    morse_dict = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--.."
    }
    morse_text = ''
    input_licence = input_licence.lower()
    for i in input_licence:
        for j in morse_dict.keys():
            if i == j:
                morse_text += morse_dict[i] + ' '
    return (morse_text)


def main():
    input_licence = input().strip()  # Enter license plate
    plate_check = check(input_licence.upper())
    print(plate_check)
    if plate_check.startswith('forbidden') == True:
        exit()
    format_name = input().strip().lower()  # 'Enter format
    if format_name == 'nato':
        plate_format = nato(input_licence)
        print(plate_format)
    elif format_name == 'ascii':
        plate_format = ascii(input_licence)
        print(plate_format)
    elif format_name == 'morse':
        plate_format = morse(input_licence)
        print(plate_format)
    else:
        print('Wrong format!')


if __name__ == '__main__':
    main()