# author: Paolo Gübeli
# version: 05.10.2020
import math

if __name__ == '__main__':
    # I check if the inputs are integer numbers
    while True:
        # I ask for two numbers.
        num1 = input("Insert a number between 0 and 100: ")

        if num1.isnumeric():
            break
        else:
            print("Insert a number not a string Thx")

    num1 = int(num1)
    if 0 <= num1 <= 100:
        perc = int((num1-1) / 10)

        print(f"The number ({num1}) is in the range between {perc * 10 + math.ceil(perc / 10)} and {perc * 10 + 10}.")

    else:
        print(f"The number ({num1}) is not in the range between 0 and 100.")

