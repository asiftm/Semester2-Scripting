import time
import datetime


def zodiac(day, month):
    print('hi')


def percentage(day, month):
    print('hi')


def historical(day, month):
    print('hi')


def one(day, month, year):
    print('hi')


def wikipedia(day, month):
    print('hi')


def age(day, month, year):
    birthdate = datetime.datetime.strptime(f"{year}-{month}-{day}","%Y-%m-%d").date()
    current_date = datetime.date.today()
    age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))
    print(f"Today {age} years old!")


def convert_date_format(date_string):
    date_formats = ['%Y/%m/%d', '%m-%d-%Y', '%Y-%m-%d', '%m/%d/%Y', '%d-%m-%Y', '%d/%m/%Y', '%d %B %Y','%m-%d-%y','%B %d, %Y']
    for date_format in date_formats:
        try:
            date_obj = datetime.datetime.strptime(date_string, date_format)
            new_date_string = date_obj.strftime("%Y-%m-%d")
            return new_date_string
        except ValueError:
            pass
    return "Invalid date format!"

def main():
    input_birthdate = '     14 january 1980     '  # input()
    birthdate = convert_date_format(input_birthdate.strip())
    if birthdate == 'Invalid date format!':
        print('Invalid date format!')
        exit()
    execution_manner = 'single'  # input().lower().split()

    if execution_manner == 'single':
        # age
        bDay = birthdate.split('-')[2]
        bMonth = birthdate.split('-')[1]
        bYear = birthdate.split('-')[0]
        age(bDay, bMonth, bYear)

    elif execution_manner == 'multi':
        print("")


if __name__ == "__main__":
    main()
