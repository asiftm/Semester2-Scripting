# import datetime

# def calculate_birthyear(age):
#     return(datetime.date.today().year)-age

# age = int(input("what is your age? : "))
# birthday = calculate_birthyear(age)
# print(f"if you born in the {birthday}, then your age is {age}. and todays date is {datetime.date.today()}")


import datetime

def calculate_birthyear(age):
    return(datetime.date.today().year)-age

age = int (input('how old are you?'))
birthday = calculate_birthyear(age)
print(f'you born in {birthday}')
