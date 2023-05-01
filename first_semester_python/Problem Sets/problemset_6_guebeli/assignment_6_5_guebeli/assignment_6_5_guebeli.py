if __name__ == '__main__':

    numbers = []

    for i in range(7):
        while True:
            try:
                number = float((input("Insert a positive number: ")))
                if number >= 0:
                    numbers.append(number)
                    break
                else:
                    print("The number is negative!")
            except ValueError:
                print("Insert a valid number!")

    print(f"\nMinimum: {min(numbers)}\nMaximum: {max(numbers)}\nMean: {sum(numbers)/len(numbers)}")

