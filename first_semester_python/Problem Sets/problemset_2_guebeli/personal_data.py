# Exercise 2.2
# author Paolo Gübeli
# version 21.09.2020

import datetime

if __name__ == '__main__':
    name = input("Insert your name: ")
    surname = input("Insert your surname: ")
    address = input("Insert your address: ")

    while True:
        year = input("Insert your birth year: ")

        if year.isnumeric():
            break

        else:
            print("Insert a number not a string Thx")

    now = datetime.datetime.now()
    year = int(year)
    age = now.year - year

    print(f"First Name: "+name+"\n"
            "Last Name: "+surname+"\n"
            "Address: "+address+"\n"
            "Year of Birth: "+str(year)+"\n"
            "Age: "+str(age)+"\n")