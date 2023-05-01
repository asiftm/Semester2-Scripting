# author: Paolo Gübeli
# version: 28.09.2020

import math

# I define the main.
if __name__ == '__main__':

    # I check if the input is really a float
    while True:
        # I ask for the radius.
        rad = input("Insert circle's radius: ")

        try:
            rad = float(rad)
            if rad > 0:
                break
            else:
                print("Insert a valid radius. Thx")

        except ValueError:
            print("Insert a number not a string. Thx")

    print(f"Diameter: {rad*2}")
    print(f"Circumference: {math.pi*rad*2}")
    print(f"Area: {math.pi*(rad**2)}")




