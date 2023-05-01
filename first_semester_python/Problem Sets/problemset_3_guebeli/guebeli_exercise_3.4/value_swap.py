# author: Paolo Gübeli
# version: 28.09.2020

# I define the main.
if __name__ == '__main__':

    # I ask for two values.
    val1 = input("Insert a value: ")
    val2 = input("Insert another value: ")

    # I print the values.
    print(f"Values before swapping:\n\tFirst Value: {val1}\n\tSecond Value: {val2}")

    # I swap the 2_variables.ipynb
    swap_var = val1
    val1 = val2
    val2 = swap_var

    # I print the 2_variables.ipynb again.
    print(f"Values after swapping:\n\tFirst Value: {val1}\n\tSecond Value: {val2}")



