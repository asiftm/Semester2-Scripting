

if __name__ == '__main__':
    phrase = list(input("Text: ").lower())

    counter = {}

    for letter in phrase:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1

    for k in sorted(counter):
        print(f"{k} : {counter[k]}")