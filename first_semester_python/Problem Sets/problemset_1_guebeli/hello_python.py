import numpy

if __name__ == "__main__":
    # request user input
    name = input("What is your name?: ")
    print("Hi " + name.strip() + " welcome to the course")
    while True:
        num1 = input("Insert an integer number: ")
        num2 = input("Insert another integer number: ")

        if isinstance(num1, int) and isinstance(num2, int):
            break

        else:
            print("Insert a number not a string Thx")

    num1 = int(num1)
    num2 = int(num2)


    # do calculations
    num_sum = num1 + num2
    num_diff = num1 - num2
    num_multi = num1 * num2

    # print results
    print(str(num1) + " + " + str(num2) + " = " + str(num_sum))
    print(str(num1) + " - " + str(num2) + " = " + str(num_diff))
    print(str(num1) + " * " + str(num2) + " = " + str( num_multi ))
    