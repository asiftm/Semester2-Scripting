import requests
from bs4 import BeautifulSoup
import random

def rand():
    url = 'https://www.196flavors.com/most-popular-cambodian-recipes/'
    response = requests.get(url)
    code = response.text
    soup = BeautifulSoup(code, 'html.parser')

    tags = soup.find_all('div', {'class': 'wprm-recipe-roundup-summary-container'})

    link_list = []

    for i in tags:
        a = (str(i).split('\n')[4].split(' '))
        for j in a:
            if j.startswith('href'):
                link_list.append(j.split('"')[1])

    random_link = random.choice(link_list)

    response = requests.get(random_link)
    code = response.text
    soup = BeautifulSoup(code, 'html.parser')

    header = soup.find('h1', {'class': 'entry-title'})
    print("------------------",header.text,"--------------------")

    print('\nIngredients')
    ing = soup.find_all('li', {'class': 'wprm-recipe-ingredient'})
    for i in ing:
        print(f'- {i.text}')

    print('\nMethod')
    int = soup.find_all('li', {'class': 'wprm-recipe-instruction'})
    counter = 1
    for i in int:
        print(f'{counter}. {i.text}')
        counter += 1

choice = input("""Would you like to make a Cambodian delicacy?
1. Yes
2. No
""")
print("\n")

if choice == "Yes":
    rand()
elif choice == "No":
    print("See you next time")
    exit()
else:
    print("Please choose a valid input")