# author: Paolo Gübeli
# version: 05.10.2020
import math

if __name__ == '__main__':

    # I check if the inputs are float numbers
    while True:
        # I ask for two numbers.
        num1 = input("First side: ")
        num2 = input("Second side: ")
        angle = input("The angle between them: ")

        try:
            num1 = float(num1)
            num2 = float(num2)
            angle = float(angle)
            break
        except ValueError:
            print("Insert numbers not strings Thx")

    print(f"The 3rd side length is: {math.sqrt(num1*num1 + num2*num2 - 2*num1*num2*math.cos(math.radians(angle)))}.")
