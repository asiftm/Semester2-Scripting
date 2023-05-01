
if __name__ == '__main__':

    words = []

    for i in range(10):
        words.append(input("Insert a word: "))

    find = input("Insert the word to find: ")

    for i in words:
        print(f"Word {words.index(i)+1} = {i}")

    try:
        index = words.index(find)
    except ValueError:
        print("\nThat word is not in the list!")
    else:
        print(f"\nThe word found is the number {index + 1} and is at the index {index} of the list.")


