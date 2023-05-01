

if __name__ == '__main__':

    fld = []
    sld = []

    print("List of words in the first language: ")
    for i in range(5):
        fld.append(input(""))

    print("List of words in the second language: ")
    for i in range(5):
        sld.append(input(""))

    translator = dict(zip(fld, sld))

    while True:
        word = input("Word to translate: ")
        if word in translator:
            print(f"Translated word: {translator[word]}")
        elif word == "-1":
            print("Stop!")
            break
        else:
            word_translated = input("Insert translated word: ")
            translator[word] = word_translated
            print("Dictonary updated!")


