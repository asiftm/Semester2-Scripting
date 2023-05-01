# author: Paolo Gübeli
# version: 05.10.2020

# I define the main.
if __name__ == '__main__':

    # I check if the inputs are integer numbers
    while True:
        # I ask for two numbers.
        num1 = input("Insert a number: ")
        num2 = input("Insert a second number: ")

        if num1.isnumeric() and num2.isnumeric():
            break

        else:
            print("Insert numbers not strings Thx")

    # I cast the inputs in integers.
    num1 = int(num1)
    num2 = int(num2)

    # I print the results of the operations.
    if (num1 % num2) == 0:
        print(f"The result of the division is: {int(num1/num2)}")

    if num1 > num2:
        print(f"{num1} is bigger than {num2}")
    elif num1 < num2:
        print(f"{num1} is smaller than {num2}")
    else:
        print("The two numbers are equal.")

    if (num1-num2) > (num2-num1):
        print(f"The difference ({num1}-{num2}) is bigger than ({num2}-{num1})")
    elif (num1-num2) < (num2-num1):
        print(f"The difference ({num1}-{num2}) is smaller than ({num2}-{num1})")