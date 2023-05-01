# author: Paolo Gübeli
# version: 28.09.2020

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

    # I print the question and the result of the operation.
    print("Is the first number a multiple of the second? ")
    print((num1 % num2) == 0)

