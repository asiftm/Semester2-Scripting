from bs4 import BeautifulSoup
import requests

recipe_dict = {}  # each recipe will be in this dict which will be added to the all_recipes list. the key of this dict is recipe name and the value is ingredients and procedures
ingredients_procedure_lst = []  # this list will have two items, all ingredients and procedure
ingredients = ''
procedure = ''
recipe_name = ''

# # one (6)
# # https://www.visitrwandaguide.com/food/rwanda-food-cuisine-recipes/
# url = 'https://www.visitrwandaguide.com/food/rwanda-food-cuisine-recipes/'
# response = requests.get(url)
# html_txt = response.text
# soup = BeautifulSoup(html_txt, 'html.parser')
# table_body_tag = soup.find_all('tbody')
# for tag in table_body_tag:
#     for i in tag.text.split('Ø'):
#         full_txt = (i.strip().split('Ingredients'))
#         if len(full_txt) > 1:
#             recipe_name = full_txt[0].strip()
#
#             ingredients_procedure = (full_txt[1].strip().split('Procedure:'))
#             ingredients = ingredients_procedure[0].replace(':\n', '').replace(': \n', '').strip()
#             procedure = ingredients_procedure[1].replace(
#                 '\nTry a Rwandan dish today and tell me the results tomorrow!!!', '').strip()
#
#             ingredients_procedure_lst.append(ingredients)
#             ingredients_procedure_lst.append(procedure)
#             recipe_dict[recipe_name] = ingredients_procedure_lst
#
#             ingredients_procedure_lst = []
#             ingredients = ''
#             procedure = ''
#             recipe_name = ''
#
# # two (3)
# # https://www.internationalcuisine.com/category/rwanda/
# lst = ['rwandan-hard-boiled-eggs', 'rwandan-goat-brochettes', 'rwandan-mandazi']
# for i in lst:
#     ingredients_procedure_lst = []
#     ingredients = ''
#     procedure = ''
#     recipe_name = ''
#
#     url = f'https://www.internationalcuisine.com/{i}/'
#     response = requests.get(url)
#     html_txt = response.text
#     soup = BeautifulSoup(html_txt, 'html.parser')
#
#     # recipe_name
#     name_tags = soup.find('h2', {'class': 'wprm-recipe-name wprm-block-text-bold'})
#     recipe_name = name_tags.text.replace('Rwandan ', '')
#
#     # ingredients
#     ingredients_tags = soup.find_all('li', {'class': 'wprm-recipe-ingredient'})
#     txt = ''
#     for tag in ingredients_tags:
#         txt = txt + tag.text + ','
#     ingredients = txt.rstrip(', ')
#
#     # procedure
#     procedure_tags = soup.find_all('div', {'class': 'wprm-recipe-instruction-text'})
#     txt = ''
#     for tag in procedure_tags:
#         txt = txt + tag.text + ' '
#     procedure = txt.strip()
#
#     ingredients_procedure_lst.append(ingredients)
#     ingredients_procedure_lst.append(procedure)
#     recipe_dict[recipe_name] = ingredients_procedure_lst
#
# # three
# # https://www.food.com/recipe/rwandan-chicken-457010?ic1=suggestedAsset%7Crwandan
# ingredients_procedure_lst = []
# ingredients = ''
# procedure = ''
# recipe_name = ''
#
# url = 'https://www.food.com/recipe/rwandan-chicken-457010?ic1=suggestedAsset%7Crwandan'
# response = requests.get(url)
# html_txt = response.text
# soup = BeautifulSoup(html_txt,'html.parser')
#
# # recipe_name
# name_tags = soup.find('h1', {'class': 'svelte-1muv3s8'})
# recipe_name = name_tags.text
#
# # ingredients
# ingredients_tags = soup.find_all('li', {'style': 'display: contents'})
# txt = ''
# for i in ingredients_tags:
#     txt = txt + i.text.replace(',','').replace('\n\n\n','').replace('  ',' ').replace('\n','').replace('  ',' ').strip() + ', '
# ingredients = txt.rstrip(', ')
# ingredients_procedure_lst.append(ingredients)
#
# # procedure
# procedure_tags = soup.find_all('li', {'class': 'direction svelte-ovaflp'})
# txt = ''
# for tag in procedure_tags:
#     txt = txt + tag.text + ' '
# procedure = txt.rstrip(' ')
# ingredients_procedure_lst.append(procedure)
#
# recipe_dict[recipe_name] = ingredients_procedure_lst
#
#
# # four(1)
# # https://www.goway.com/travel-information/africa-middle-east/rwanda/food-and-drink/
# ingredients_procedure_lst = []
# ingredients = ''
# procedure = ''
# recipe_name = ''
#
# url = 'https://healthiersteps.com/recipe/matoke-recipe/'
# response = requests.get(url)
# html_txt = response.text
# soup = BeautifulSoup(html_txt, 'html.parser')
#
# # recipe_name
# name_tag = soup.find('h1',{'itemprop':'headline'})
# recipe_name = name_tag.text.split(' ')[0]
#
# # ingredients
# ingredients_tags = soup.find_all('strong')
# txt = ''
# for i in ingredients_tags:
#     if ':' in i.text and 'Step' not in i.text:
#         txt = txt + (i.text.replace(':', '')) + ', '
# ingredients = txt.rstrip(', ')
# ingredients_procedure_lst.append(ingredients)
#
# # procedures
# txt = ''
# procedure_tags = soup.find_all('p')
# for i in procedure_tags:
#     if i.text.startswith('Step'):
#         txt = txt + i.text.split(': ')[1] + '\n'
# procedure = txt.rstrip('\n')
# ingredients_procedure_lst.append(procedure)
#
# recipe_dict[recipe_name] = ingredients_procedure_lst

# five(1)
# https://afrogistmedia.com/ibihaza-recipe-rwandese-cuisine

url = 'https://afrogistmedia.com/ibihaza-recipe-rwandese-cuisine'
response = requests.get(url)
print(response)
html_txt = response.text
soup = BeautifulSoup(html_txt, 'html.parser')
print(soup)
# recipe_name
name_tag = soup.find('h1',{'class':'entry-title'})
# print(name_tag.text.split(' ')[0])
print(name_tag)


for x,y in recipe_dict.items():
    print(x)
    print('           ingredients :')
    for i in y[0].split(','):
        if i != '':
            print(i.strip())
    print('           method :')
    for i in y[1].split('.'):
        if i != '':
            print(i.strip())

# print(len(recipe_dict))
