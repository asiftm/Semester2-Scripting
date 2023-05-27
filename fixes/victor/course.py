import requests
from bs4 import BeautifulSoup
import random


def lunch():
    lunch_list = ["https://ourbigescape.com/great-cambodian-num-bahn-chok-recipes/",
                  "https://ourbigescape.com/best-cambodian-samlor-kako-recipes/",
                  "https://ourbigescape.com/easy-bai-sach-chrouk-recipe/",
                  "https://ourbigescape.com/simple-cambodian-kroeung-recipe/",
                  "https://ourbigescape.com/simple-and-easy-cambodian-roti-recipe/"]

    random_link = random.choice(lunch_list)

    response = requests.get(random_link)
    code = response.text
    soup = BeautifulSoup(code, 'html.parser')

    tags = soup.find_all('h3')
    for i in tags:
        if i.text.startswith('How To'):
            header = i.text.replace('How To Make Our Cambodian ', '').replace(' Recipe', '')

    print("------------------", header, "--------------------", '\n')

    tags = soup.find('div', {'class': 'entry-content clear'})
    lst = tags.text.split('\n')
    con1 = False
    con2 = False
    for i in lst:

        if con2:
            if i.startswith('Nutri'):
                break
            print(i)

        if i.strip().startswith('Instructions'):
            print('\nInstructions')
            con1 = False
            con2 = True

        if con1:
            print('-', i)

        if i.strip().startswith('Ingredients'):
            print('Ingredients')
            con1 = True


def dinner():
    dinner_list = ["https://ourbigescape.com/great-cambodian-lok-lak-recipe/",
                   "https://ourbigescape.com/great-cambodian-lemongrass-chicken-recipe/",
                   "https://ourbigescape.com/best-cambodian-fish-amok/",
                   "https://ourbigescape.com/best-cambodian-samlor-kako-recipes/",
                   "https://ourbigescape.com/quick-and-easy-cambodian-lort-cha-recipe/"]

    random_link = random.choice(dinner_list)

    response = requests.get(random_link)
    code = response.text
    soup = BeautifulSoup(code, 'html.parser')

    tags = soup.find_all('h3')
    for i in tags:
        if i.text.startswith('How To'):
            header = i.text.replace('How To Make Our Cambodian ', '').replace(' Recipe', '')

    print("------------------", header, "--------------------", '\n')

    tags = soup.find('div', {'class': 'entry-content clear'})
    lst = tags.text.split('\n')
    con1 = False
    con2 = False
    for i in lst:

        if con2:
            if i.startswith('Nutri'):
                break
            print(i)

        if i.strip().startswith('Instructions'):
            print('\nInstructions')
            con1 = False
            con2 = True

        if con1:
            print('-', i)

        if i.strip().startswith('Ingredients'):
            print('Ingredients')
            con1 = True


def breakfast():
    breakfast_list = ["https://www.196flavors.com/cambodia-num-poum/",
                      "https://www.196flavors.com/bo-luc-lac/",
                      "https://www.196flavors.com/khao-poon-kapoon/",
                      "https://www.196flavors.com/cambodia-kuy-teav/", ]

    random_link = random.choice(breakfast_list)

    response = requests.get(random_link)
    code = response.text
    soup = BeautifulSoup(code, 'html.parser')

    tags = soup.find_all('h3')
    for i in tags:
        if i.text.startswith('How To'):
            header = i.text.replace('How To Make Our Cambodian ', '').replace(' Recipe', '')

    print("------------------", header, "--------------------", '\n')

    tags = soup.find('div', {'class': 'entry-content clear'})
    lst = tags.text.split('\n')
    con1 = False
    con2 = False
    for i in lst:

        if con2:
            if i.startswith('Nutri'):
                break
            print(i)

        if i.strip().startswith('Instructions'):
            print('\nInstructions')
            con1 = False
            con2 = True

        if con1:
            print('-', i)

        if i.strip().startswith('Ingredients'):
            print('Ingredients')
            con1 = True


choice = int(input("""For which courses would you like have a recipe: 
1. Breakfast
2. Lunch
3. Dinner
Choose a number: """))
print("\n")
if choice == 1:
    lunch()
elif choice == 2:
    lunch()
elif choice == 3:
    dinner()
else:
    print("Please make a valid choice")

# Continue with Dinner and Breakfast after this
