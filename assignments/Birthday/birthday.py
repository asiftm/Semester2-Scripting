import time
import datetime
import requests
from bs4 import BeautifulSoup
import json


def zodiac(day, month):
    month_name = get_month_name(month)
    url = f'https://takemeback.to/{day}-{month_name}'
    r = requests.get(url)
    html_code = r.text
    soup = BeautifulSoup(html_code, 'html.parser')
    tag_lst = soup.find_all('p', {'itemprop': 'text'})
    for i in tag_lst:
        zodiac_sign = (i.getText().split('\n')[1].strip().split(' ')[-1].replace('.', ''))
    print(f'Zodiac sign: {zodiac_sign}')


def percentage(day, month):
    print('hi')


def historical(day, month):
    api_url = f'https://api.api-ninjas.com/v1/historicalevents?month={month}&day={day}'
    response = requests.get(api_url, headers={'X-Api-Key': 'J0ceLW0KRsLq43YArvevjQ==1d2uXMtpipaBLTc0'})
    json_data = json.loads(response.text)
    for i in json_data:
        print(i['year'] + ' - ' + i['event'])


def one(day, month, year):
    month_name = get_month_name(month)
    url = f'https://www.onthisday.com/date/{year}/{month_name}/{day}'
    r = requests.get(url)
    html_code = r.text
    soup = BeautifulSoup(html_code, 'html.parser')
    tag_lst = soup.find_all('li', {'class': 'event'})

    for i in tag_lst:
        if ('img alt="US"' in str(i)):
            print('Number one hit: ', (i.getText()).replace(' #1 Song: ', ''))


def wikipedia(day, month):
    print('hi')


def age(day, month, year):
    birthdate = datetime.datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d").date()
    current_date = datetime.date.today()
    age = current_date.year - birthdate.year - (
            (current_date.month, current_date.day) < (birthdate.month, birthdate.day))
    print(f"Today {age} years old!")


def convert_date_format(date_string):
    date_formats = ['%Y/%m/%d', '%m-%d-%Y', '%Y-%m-%d', '%m/%d/%Y', '%d-%m-%Y', '%d/%m/%Y', '%d %B %Y', '%m-%d-%y',
                    '%B %d, %Y']
    for date_format in date_formats:
        try:
            date_obj = datetime.datetime.strptime(date_string, date_format)
            new_date_string = date_obj.strftime("%Y-%m-%d")
            return new_date_string
        except ValueError:
            pass
    return "Invalid date format!"


def get_month_name(month_number):
    months = {
        '01': "January",
        '02': "February",
        '03': "March",
        '04': "April",
        '05': "May",
        '06': "June",
        '07': "July",
        '08': "August",
        '09': "September",
        '10': "October",
        '11': "November",
        '12': "December"
    }
    return months[f'{month_number}']


def main():
    input_birthdate = '     14 January 1980     '  # input()
    execution_manner = 'single'  # input().lower().split()

    birthdate = convert_date_format(input_birthdate.strip())
    if birthdate == 'Invalid date format!':
        print('Invalid date format!')
        exit()
    bDay = birthdate.split('-')[2]
    bMonth = birthdate.split('-')[1]
    bYear = birthdate.split('-')[0]

    if execution_manner == 'single':
        # age
        age(bDay, bMonth, bYear)
        # zodiac
        zodiac(bDay, bMonth)
        # historical
        historical(bDay, bMonth)
        # one
        one(bDay,bMonth,bYear)


    elif execution_manner == 'multi':
        print("")


if __name__ == "__main__":
    main()
