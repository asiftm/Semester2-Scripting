from bs4 import BeautifulSoup
import requests
import birthday
month = 2
day = 3

month_name = birthday.get_month_name(month)
url = f'https://en.wikipedia.org/wiki/{month_name}_{day}'
response = requests.get(url)
html_code = response.text
soup = BeautifulSoup(html_code, 'html.parser')
tags = soup.find_all('div', {'class': 'mw-parser-output'})
print(tags)
temp_lst = (tags[1].getText().split('\n'))
birth_lst = []
condition = False;

file = open(f'{month_name}_{day}.txt', 'w')

for i in temp_lst:
    if i.strip() == 'Deaths[edit]':
        break
    if condition and '[edit]' not in i:
        file.write(f'{i}\n')
    if i.strip() == 'Births[edit]':
        condition = True
file.close()
print(f'File saved as {month_name}_{day}.txt')