age = input("what is your age? ")

if age.isnumeric():
    age = int(age)

    if age < 12:
        print("not allowed")
    elif age < 15:
        print("avoid it")
    elif age < 18:
        print("somehow allowed")
    else:
        print("allowed")
else:
    print("wrong input")