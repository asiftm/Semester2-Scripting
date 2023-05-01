import re
import art

def forbidden(plate):
    forbidden_patterns = [
        'AAP', 'AAS', 'AEL', 'ALA', 'ANE', 'ASS', 'BEB', 'BIT', 'BOM', 'BOY',
        'BSP', 'BUB', 'BWP', 'BYT', 'CAP', 'CDF', 'CDH', 'CDV', 'CON', 'CSP',
        'CUB', 'CUL', 'CUT', 'CVP', 'DCD', 'DIK', 'DOM', 'FDF', 'FOK', 'FOL',
        'FOU', 'FUC', 'FUK', 'GAT', 'GAY', 'GEK', 'GOD', 'HIV', 'HOL', 'JEK',
        'KAK', 'KKQ', 'KUL', 'KUT', 'LAF', 'LDD', 'LSP', 'LUL', 'MAS', 'MCC',
        'MDP', 'MOR', 'MOU', 'MST', 'NIC', 'NIK', 'NIQ', 'NVA', 'PDB', 'PDO',
        'PET', 'PFF', 'PIK', 'PIN', 'PIP', 'PIS', 'PJU', 'PKK', 'POT', 'PRL',
        'PSB', 'PSC', 'PSL', 'PTB', 'PUE', 'PUT', 'PVV', 'PYK', 'PYN', 'PYP',
        'PYS', 'ROM', 'SEX', 'SOA', 'SOT', 'SPA', 'SUL', 'TAK', 'TET', 'TIT',
        'TUE', 'VCD', 'VIH', 'VLD', 'VMO', 'VNV', 'ZAC', 'ZAK', 'ZOT'
    ]

    flag = False
    for forbid in forbidden_patterns:
        if forbid in plate:
            flag = True
            break
    return flag

def check(plate):

    forbi = forbidden(plate)
    if forbi == True:
        return True


    # 1962-1971: AA.001 → ZZ.999
    pattern1 = r"([A-Z]{2})\.\d{3}\b"

    # 1971-1973: A.001.A → Z.999.Z
    pattern2 = r"[A-Z]\.\d{3}\.[A-Z]\b"

    # 1973-2008: AAA-001 → ZZZ-999
    pattern3 = r"[A-Z]+.[A-Z]{3}\-\d{3}\b"

    # 2008-2010: 001-AAA → 999-CFQ
    pattern4 = r"\d{3}-[A-C][A-F][A-Q]\b"

    # 2010-now: 1-AAA-001 → 7-ZZZ-999
    pattern5 = r"\d{1}\-[A-Z]{3}\-\d{3}\b"

    # 1-9: vehicle from king and/or queen (output kind and queen)
    Sp_pattern_1 = r"[1-9]\b"

    # 10-99: vehicles from other royal family members (output royal)
    Sp_pattern_2 = r"\b([1-9][0-9])\b"

    # A-1 → A-999: official (vehicles)
    Sp_pattern_3 = r"A\-[1-999]\b"

    # CD-AA111 → CD-ZZ999: diplomat (vehicles)
    Sp_pattern_4 = r"^CD-[A-Z]{2}\d{3}\b"

    # G-LAA-111 → G-LZZ-999: agriculture  (vehicles)
    Sp_pattern_5 = r"^G-L[A-Z]{2}-\d{3}\b"

    # M-AAA-000 → M-ZZZ-999: motorcycle(s)
    Sp_pattern_6 = r"^M-[A-Z]{3}-\d{3}\b"

    # O-AAA-111 → O-ZZZ-999: oldtimer(s)
    Sp_pattern_7 = r"^O-[A-Z]{3}-\d{3}\b"

    # Q-AAA-000 → Q-ZZZ-999: trailer(s)
    Sp_pattern_8 = r"^Q-[A-Z]{3}-\d{3}\b"

    # T-XAA-000 → T-XZZ-999: taxi(s)
    Sp_pattern_9 = r"^T\-X[A-Z]{2}\-\d{3}\b"

    # Y-AAA-000 → Y-ZZZ-999: test (drives)
    Sp_pattern_10 = r"^Y\-[A-Z]{3}\-\d{3}\b"


    if re.match(pattern1, plate):
        return ("standard plate - 1962-1971")  # 1962-1971: AA.001 → ZZ.999

    elif re.match(pattern2, plate):
        return ("standard plate - 1971-1973")  # 1971-1973: A.001.A → Z.999.Z

    elif re.match(pattern3, plate):
        return("standard plate - 1973-2008")  # 1973-2008: AAA-001 → ZZZ-999

    elif re.match(pattern4, plate):
        return("standard plate - 2008-2010")

    elif re.match(pattern5, plate):
        return("standard plate - 2010-now")

    elif re.match(Sp_pattern_1, plate):
        return("Special plate - king and queen")

    elif re.match(Sp_pattern_2, plate):
        return("Special plate - Royal")

    elif re.match(Sp_pattern_3, plate):
        return("standard plate - official (vehicles)") # official (vehicles)

    elif re.match(Sp_pattern_4, plate):
        return("standard plate - diplomat (vehicles)")# diplomat (vehicles)

    elif re.match(Sp_pattern_5, plate):
        return("standard plate -  agriculture (vehicles)")

    elif re.match(Sp_pattern_6, plate):
        return("standard plate -  motorcycle(s)")

    elif re.match(Sp_pattern_7, plate):
        return("standard plate - oldtimer(s)")

    elif re.match(Sp_pattern_8, plate):
        return("standard plate -   trailer(s)")

    elif re.match(Sp_pattern_9, plate):
        return("standard plate -   taxi(s)")

    elif re.match(Sp_pattern_10, plate):
        return("standard plate -   test (drives)")  # test (drives)
    else:
        return 'invalid plate'

def morse(plate):
    morse_code = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.'
    }

    for char in plate:
        if char in morse_code:
            print (morse_code[char], end=' ')

def nato(plate):
    return '.'

def ascii(plate):
    ascii_art = art.text2art(plate)
    return ascii_art

def main():
    input_plate=input()
    check_plate=check(input_plate)
    if check_plate==True:
        a=input_plate.split('-')
        for i in a:
            if len(i)==3 and i.isalpha():
                print(f'forbidden plate - {i}')
                exit()

    print(check_plate)

    art = input()
    if art == "ascii":
        print(ascii(input_plate))
    elif art == "nato":
        print(nato(input_plate))
    elif art == "morse":
        print(morse(input_plate))
    else:
        print("Wrong format!")


if __name__=='__main__':
    main()



