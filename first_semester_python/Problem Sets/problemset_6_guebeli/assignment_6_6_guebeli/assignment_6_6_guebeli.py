
if __name__ == '__main__':

    words = []

    for i in range(10):
        words.append(input("Insert a word: "))

    print(f"\nOriginal order:\n{words}\n")
    words.reverse()
    print(f"Reversed order:\n{words}\n")
    words.sort()
    print(f"\nAlphabetical order:\n{words}\n")
    words.sort(reverse=True)
    print(f"Reversed alphabetical order:\n{words}")

    words_dp = list(dict.fromkeys(words))
    print("Count:")
    for i in words_dp:
        print(f"{i}: {words.count(i)}")

