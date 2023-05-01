# author: Paolo Gübeli
# version: 05.10.2020

if __name__ == '__main__':
    # I check if the inputs are valid numbers
    while True:
        # I ask for the values.
        engine = input("Insert the engine's type: ")
        length = input("Insert the aircraft's length: ")

        try:
            engine = int(engine)
            length = float(length)
            break
        except ValueError:
            print("Insert valid numbers not strings Thx")

    if engine == 1 and length >= 20:
        print("The maximum pressure is 200 bar.")
    elif (engine == 2 and 10 < length <= 20) or (engine == 1 and length < 20):
        print("The maximum pressure is 150 bar.")
    elif engine == 3 and length < 10:
        print("The maximum pressure is 100 bar.")
    else:
        print("The maximum pressure is 50 bar.")
