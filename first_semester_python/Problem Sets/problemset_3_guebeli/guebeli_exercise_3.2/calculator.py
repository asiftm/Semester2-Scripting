# author: Paolo Gübeli
# version: 28.09.2020

# I define the main.
if __name__ == '__main__':

    # I check if the inputs are float numbers
    while True:
        # I ask for two numbers.
        num1 = input("First value: ")
        num2 = input("Second Value: ")

        try:
            num1 = float(num1)
            num2 = float(num2)
            break
        except ValueError:
            print("Insert numbers not strings Thx")

    # I print the question and the result of the operation.
    print(f"Sum: {num1} + {num2} = " + str(num1 + num2))
    print(f"Difference: {num1} - {num2} = " + str(num1 - num2))
    print(f"Product: {num1} * {num2} = " + str(num1 * num2))
    print(f"Quotient: {num1} / {num2} = " + str(num1 / num2))

