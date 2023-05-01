# Exercise 2.3
# author Paolo Gübeli
# version 21.09.2020

if __name__ == '__main__':

    while True:
        num1 = input("Insert a number: ")
        num2 = input("Insert another number: ")
        num3 = input("Insert a last number: ")

        if num1.isnumeric() and  num2.isnumeric() and num3.isnumeric() :
            break

        else:
            print("Insert positive numbers not strings Thx")

    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)

    result = num1+num2-num3

    print(str(num1) + " + " + str(num2) + " - " + str(num3) + " = " + str(result))