import requests
from bs4 import BeautifulSoup
import random

all = []

recipe_list = ["saudi-saleeg", "chicken-machboos-with-baharat-sella", "bahraini-chicken-machboos", "kacchi-mutton-biryani", "cream-kunafa", "overnight-oats-recipe-guide",
                "saudi-sambosa-mung-bean-and-meat-samosas", "saudi-mutabbaq-recipe", "nammoura-or-basbousa-middle-eastern", "sweet-kataifi-truffles", "bahraini-khabees-wheat-flour-sweet-breakfast",
                "balaleet-sweet-vermicelli-and-eggs","qamar-al-din-apricot-fruit-leather-drink", "mofatah-al-dajaj-ethnic-saudi-rice-and", "fatteh-hummus-with-chicken",
                "omani-coconut-macaroons-chaklama", "kafta-bil-sanieh-recipe","bedouin-lamb-rice", "one-pot-chicken-kabsah"]

for i in recipe_list:
    single = []
    ing = []
    met = []
    url = f'https://butfirstchai.com/{i}/'
    response = requests.get(url)
    rec = response.text
    soup = BeautifulSoup(rec,'html.parser')

    header = soup.find('h1',{'class':'entry-title'}).text
    single.append(header)

    ingTag = soup.find_all('li',{'class':'wprm-recipe-ingredient'})
    for i in ingTag:
        ing.append(i.text)
    single.append(ing)

    ingTag = soup.find_all('div',{'class':'wprm-recipe-instruction-text'})
    for i in ingTag:
        met.append(i.text)
    single.append(met)

    all.append(single)

random_choice = random.choice(all)
for i in range(len(random_choice)):
    if i == 0:
        print(random_choice[i])
    if i == 1:
        print('Ingredients')
        for j in random_choice[i]:
            print(j)
    if i == 2:
        print('Method')
        for k in random_choice[i]:
            print(k)


