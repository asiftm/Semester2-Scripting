if __name__ == "__main__":
    print("Simple calculator")
    print("-----------------")

    choice = 5

    while True:
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")
        print("5 - Exit")

        # get choice

        choice = int(input("Chose the operation: "))

        if choice == 5:
            break

        print ("Insert the two numbers to use")

        while True:
            num1 = input(f"Insert an integer number: ")
            num2 = input("Insert another integer number: ")

            if num1.isnumeric() and num2.isnumeric():
                break

            else:
                print("Insert a number not a string Thx")

        num1 = int(num1)
        num2 = int(num2)

        if choice == 1:
            print(f"{num1} + {num2} = {num1 + num2}")
        elif choice == 2:
            print(f"{num1} - {num2} = {num1 - num2}")
        elif choice == 3:
            print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == 4:
            print(f"{num1} / {num2} = {num1 / num2}")

