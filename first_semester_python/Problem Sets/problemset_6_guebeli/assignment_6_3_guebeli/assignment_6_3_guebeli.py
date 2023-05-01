
if __name__ == '__main__':
    numbers = []

    for i in range(5):
        while True:
            try:
                number = float((input("Insert a number between 10 and 100 (No duplicates): ")))
                if 100 >= number >= 10 and number not in numbers:
                    numbers.append(number)
                    break
                else:
                    print("The number is duplicate or not in the range!")
            except ValueError:
                print("Insert a valid number!")

    print(f"\nNumbers:\n{numbers}")