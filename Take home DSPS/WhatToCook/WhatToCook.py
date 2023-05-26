def simple():
    import random

    dish = ''

    recipe_dict = scrape()
    random_key = random.choice(list(recipe_dict.keys()))
    random_item = recipe_dict[random_key]

    dish = dish + random_key + '\n'

    dish = dish + 'Ingredients' + '\n'
    for i in random_item[0].split(','):
        if i != '':
            dish = dish + i.strip() + '\n'

    dish = dish + 'Method' + '\n'
    for i in random_item[1].split('.'):
        if i != '':
            dish = dish + i.strip() + '\n'

    return dish


def course_specific(chosen_course):
    import random

    dish = ''

    file = open('recipe_course.csv').read().split('\n')
    course_specific_lst = []
    for i in file:
        if i.startswith(chosen_course):
            lst = i.split(',')
            for j in range(1, len(lst)):
                if len(lst[j]) > 0:
                    course_specific_lst.append(lst[j])

    recipe_dict = scrape()
    random_key = random.choice(list(recipe_dict.keys()))
    while random_key not in course_specific_lst:
        random_key = random.choice(list(recipe_dict.keys()))

    random_item = recipe_dict[random_key]

    dish = dish + random_key + '\n'

    dish = dish + 'Ingredients' + '\n'
    for i in random_item[0].split(','):
        if i != '':
            dish = dish + i.strip() + '\n'

    dish = dish + 'Method' + '\n'
    for i in random_item[1].split('.'):
        if i != '':
            dish = dish + i.strip() + '\n'

    return dish


def seasonal():
    import datetime
    dish = ''

    current_month = datetime.datetime.now().strftime("%B")
    file = open('vegetable.csv').read().split('\n')
    for i in file:
        if i.startswith(current_month):
            ingredients = i.rstrip(',').replace(f'{current_month},', '').split(',')

            condition = False
            while not condition:
                dish = simple()
                for ingredient in ingredients:
                    if ingredient.strip().lower() in dish:
                        condition = True
    return dish


def combined(chosen_course):
    import datetime
    current_month = datetime.datetime.now().strftime("%B")
    file = open('vegetable.csv').read().split('\n')
    dish = ''
    condition_season = False
    while not condition_season:
        dish = course_specific(chosen_course)
        for i in file:
            if i.startswith(current_month):
                ingredients = i.rstrip(',').replace(f'{current_month},', '').split(',')
                condition_course = False
                while not condition_course:
                    for ingredient in ingredients:
                        if ingredient.strip().lower() in dish:
                            condition_course = True
                            break
    return dish


def scrape():
    from bs4 import BeautifulSoup
    import requests

    recipe_dict = {}  # each recipe will be in this dict which will be added to the all_recipes list. the key of this dict is recipe name and the value is ingredients and procedures

    ingredients_procedure_lst = []  # this list will have two items, all ingredients and procedure
    ingredients = ''
    procedure = ''
    recipe_name = ''

    # one (6)
    try:
        # https://www.visitrwandaguide.com/food/rwanda-food-cuisine-recipes/
        url = 'https://www.visitrwandaguide.com/food/rwanda-food-cuisine-recipes/'
        response = requests.get(url)
        html_txt = response.text
        soup = BeautifulSoup(html_txt, 'html.parser')
        table_body_tag = soup.find_all('tbody')
        for tag in table_body_tag:
            for i in tag.text.split('Ø'):
                full_txt = (i.strip().split('Ingredients'))
                if len(full_txt) > 1:
                    # recipe_name
                    recipe_name = full_txt[0].strip()

                    ingredients_procedure = (full_txt[1].strip().split('Procedure:'))

                    # ingredients
                    ingredients_unorganized = ingredients_procedure[0].replace(':\n', '').replace(': \n',
                                                                                                  '').strip().split(
                        ', ')
                    ingredients_organized = ''
                    for i in ingredients_unorganized:
                        nxt_ingredient = False
                        for char in i:
                            if i.strip() == 'cut lengthways into 5 strips' or 'de-seeded and coarsely chopped tomato' in i.strip():
                                break
                            if char.isnumeric():
                                nxt_ingredient = True
                                ingredients_organized = ingredients_organized + ', ' + i
                                break
                        if not nxt_ingredient:
                            ingredients_organized = ingredients_organized + ' ' + i
                    ingredients = ingredients_organized.lstrip(' ,').replace('.', '')

                    # procedure
                    procedure = ingredients_procedure[1].replace(
                        '\nTry a Rwandan dish today and tell me the results tomorrow!!!', '').strip()

                    ingredients_procedure_lst.append(ingredients)
                    ingredients_procedure_lst.append(procedure)
                    recipe_dict[recipe_name] = ingredients_procedure_lst

                    ingredients_procedure_lst = []
                    ingredients = ''
                    procedure = ''
                    recipe_name = ''
    except:
        ingredients_procedure_lst = []
        ingredients = ''
        procedure = ''
        recipe_name = ''

    # two (3)
    try:
        # https://www.internationalcuisine.com/category/rwanda/
        lst = ['rwandan-hard-boiled-eggs', 'rwandan-goat-brochettes', 'rwandan-mandazi']
        for i in lst:
            ingredients_procedure_lst = []
            ingredients = ''
            procedure = ''
            recipe_name = ''

            url = f'https://www.internationalcuisine.com/{i}/'
            response = requests.get(url)
            html_txt = response.text
            soup = BeautifulSoup(html_txt, 'html.parser')

            # recipe_name
            name_tags = soup.find('h2', {'class': 'wprm-recipe-name wprm-block-text-bold'})
            recipe_name = name_tags.text.replace('Rwandan ', '')

            # ingredients
            ingredients_tags = soup.find_all('li', {'class': 'wprm-recipe-ingredient'})
            txt = ''
            for tag in ingredients_tags:
                txt = txt + tag.text + ','
            ingredients = txt.rstrip(', ')

            # procedure
            procedure_tags = soup.find_all('div', {'class': 'wprm-recipe-instruction-text'})
            txt = ''
            for tag in procedure_tags:
                txt = txt + tag.text + ' '
            procedure = txt.strip()

            ingredients_procedure_lst.append(ingredients)
            ingredients_procedure_lst.append(procedure)
            recipe_dict[recipe_name] = ingredients_procedure_lst
    except:
        ingredients_procedure_lst = []
        ingredients = ''
        procedure = ''
        recipe_name = ''

    # three(1)
    try:
        # https://www.food.com/recipe/rwandan-chicken-457010?ic1=suggestedAsset%7Crwandan
        ingredients_procedure_lst = []
        ingredients = ''
        procedure = ''
        recipe_name = ''

        url = 'https://www.food.com/recipe/rwandan-chicken-457010?ic1=suggestedAsset%7Crwandan'
        response = requests.get(url)
        html_txt = response.text
        soup = BeautifulSoup(html_txt, 'html.parser')

        # recipe_name
        name_tags = soup.find('h1', {'class': 'svelte-1muv3s8'})
        recipe_name = name_tags.text

        # ingredients
        ingredients_tags = soup.find_all('li', {'style': 'display: contents'})
        txt = ''
        for i in ingredients_tags:
            txt = txt + i.text.replace(',', '').replace('\n\n\n', '').replace('  ', ' ').replace('\n', '').replace('  ',
                                                                                                                   ' ').strip() + ', '
        ingredients = txt.rstrip(', ')
        ingredients_procedure_lst.append(ingredients)

        # procedure
        procedure_tags = soup.find_all('li', {'class': 'direction svelte-ovaflp'})
        txt = ''
        for tag in procedure_tags:
            txt = txt + tag.text + ' '
        procedure = txt.rstrip(' ')
        ingredients_procedure_lst.append(procedure)

        recipe_dict[recipe_name] = ingredients_procedure_lst
    except:
        ingredients_procedure_lst = []
        ingredients = ''
        procedure = ''
        recipe_name = ''

    # four(1)
    try:
        # https://www.goway.com/travel-information/africa-middle-east/rwanda/food-and-drink/
        ingredients_procedure_lst = []
        ingredients = ''
        procedure = ''
        recipe_name = ''

        url = 'https://healthiersteps.com/recipe/matoke-recipe/'
        response = requests.get(url)
        html_txt = response.text
        soup = BeautifulSoup(html_txt, 'html.parser')

        # recipe_name
        name_tag = soup.find('h1', {'itemprop': 'headline'})
        recipe_name = name_tag.text.split(' ')[0]

        # ingredients
        ingredients_tags = soup.find_all('strong')
        txt = ''
        for i in ingredients_tags:
            if ':' in i.text and 'Step' not in i.text:
                txt = txt + (i.text.replace(':', '')) + ', '
        ingredients = txt.rstrip(', ')
        ingredients_procedure_lst.append(ingredients)

        # procedures
        txt = ''
        procedure_tags = soup.find_all('p')
        for i in procedure_tags:
            if i.text.startswith('Step'):
                txt = txt + i.text.split(': ')[1] + '\n'
        procedure = txt.rstrip('\n')
        ingredients_procedure_lst.append(procedure)

        recipe_dict[recipe_name] = ingredients_procedure_lst
    except:
        ingredients_procedure_lst = []
        ingredients = ''
        procedure = ''
        recipe_name = ''

    # five(1)
    try:
        # https://veganphysicist.com/rwanda-vegan-agatogo/
        ingredients_procedure_lst = []
        ingredients = ''
        procedure = ''
        recipe_name = ''

        url = 'https://veganphysicist.com/rwanda-vegan-agatogo/'
        response = requests.get(url)

        html_txt = response.text
        soup = BeautifulSoup(html_txt, 'html.parser')

        # recipe_name
        recipe_name = 'Vegan agatogo'

        # ingredients
        ingredients_tags = soup.find_all('li', {'class': 'wprm-recipe-ingredient'})
        txt = ''
        for tag in ingredients_tags:
            txt = txt + tag.text.replace(',', '') + ','
        ingredients = txt.rstrip(', ')

        # procedure
        procedure_tags = soup.find_all('li', {'class': 'wprm-recipe-instruction'})
        txt = ''
        for tag in procedure_tags:
            txt = txt + tag.text + ' '
        procedure = txt.strip()

        ingredients_procedure_lst.append(ingredients)
        ingredients_procedure_lst.append(procedure)
        recipe_dict[recipe_name] = ingredients_procedure_lst
    except:
        ingredients_procedure_lst = []
        ingredients = ''
        procedure = ''
        recipe_name = ''

    # six(1)
    try:
        # https://blog.firepot.com/recipes/rwandan-ginger-tea-recipe
        ingredients_procedure_lst = []
        ingredients = ''
        procedure = ''
        recipe_name = ''

        url = 'https://blog.firepot.com/recipes/rwandan-ginger-tea-recipe'
        response = requests.get(url)

        html_txt = response.text
        soup = BeautifulSoup(html_txt, 'html.parser')

        # recipe_name
        name_tag = soup.find('div', {'class': 'title-inner-wrapper'})
        recipe_name = name_tag.text.strip().replace('Rwandan ', '').replace(' Recipe', '')

        # ingredients
        ingredients_tags = soup.find('span', {'id': 'hs_cos_wrapper_post_body'})
        txt = ''
        ingredient_condition = False
        procedure_conditon = False
        for i in (ingredients_tags.text.split('\n')):
            if procedure_conditon:
                if i[0].isnumeric():
                    txt = txt + i[3:] + ' '
                else:
                    procedure = txt.strip()
                    break

            if i.startswith('to make:'):
                ingredients = txt.rstrip(',')
                ingredient_condition = False
                txt = ''
                procedure_conditon = True

            if ingredient_condition and len(i) > 1:
                txt = txt + i + ','

            if i.startswith('You will need:'):
                ingredient_condition = True

        ingredients_procedure_lst.append(ingredients)
        ingredients_procedure_lst.append(procedure)
        recipe_dict[recipe_name] = ingredients_procedure_lst
    except:
        ingredients_procedure_lst = []
        ingredients = ''
        procedure = ''
        recipe_name = ''

    # seven (1)
    try:
        # https://www.bigoven.com/recipe/rwandan-beef/2372715
        url = 'https://www.bigoven.com/recipe/rwandan-beef/2372715'
        response = requests.get(url)
        html_txt = response.text
        soup = BeautifulSoup(html_txt, 'html.parser')

        # recipe_name
        recipe_name = soup.find('h1').text.strip()

        # ingredients
        txt = ''
        ingredient_tags = soup.find_all('span', {'class': 'ingredient'})
        for i in ingredient_tags:
            txt = txt + i.text.strip().replace('\n', ' ').replace(';  ', '; ') + ', '
        ingredients = txt.rstrip(', ')

        # procedure
        txt = ''
        procedure_tags = soup.find('div', {'class': 'instructions'}).text.replace('\n', ' ').split('.')
        for i in procedure_tags:
            txt = txt + i.strip() + '.'
        procedure = txt.strip()

        ingredients_procedure_lst.append(ingredients)
        ingredients_procedure_lst.append(procedure)
        recipe_dict[recipe_name] = ingredients_procedure_lst
    except:
        ingredients_procedure_lst = []
        ingredients = ''
        procedure = ''
        recipe_name = ''

    # eight (1)
    try:
        # https://www.supervalue.co.nz/recipes/rewena-bread/
        url = 'https://www.supervalue.co.nz/recipes/rewena-bread/'
        response = requests.get(url)
        html_txt = response.text
        soup = BeautifulSoup(html_txt, 'html.parser')

        name_tag = soup.find('h1', {'class': 'sv-recipe__heading'})
        recipe_name = name_tag.text

        # ingredients
        ingredient_tag = soup.find_all('div', {'class': 'sv-recipe__ingredients'})
        txt = ''
        for i in ingredient_tag:
            lst = i.text.split('\n')
            for j in lst:
                if j.strip() != '' and j.lower() != 'rēwena bug' and j.lower() != 'rēwena bread' and j.lower() != 'ingredients' and j.lower() != 'view method':
                    txt = txt + j.replace(',', '').strip() + ', '
        ingredients = txt.rstrip(', ')

        # procedure
        procedure_tag = soup.find_all('div', {'class': 'sv-recipe__instructions-inner'})
        txt = ''
        for i in procedure_tag:
            lst = i.text.split('\n')
            for j in lst:
                if len(j) > 40:
                    txt = txt + j.strip()
        procedure = txt.strip()

        ingredients_procedure_lst.append(ingredients)
        ingredients_procedure_lst.append(procedure)
        recipe_dict[recipe_name] = ingredients_procedure_lst
    except:
        ingredients_procedure_lst = []
        ingredients = ''
        procedure = ''
        recipe_name = ''

    # nine (1)
    try:
        # https://www.internationalcuisine.com/rwandan-sweet-potato-fries/
        url = 'https://www.internationalcuisine.com/rwandan-sweet-potato-fries/'
        response = requests.get(url)
        html_txt = response.text
        soup = BeautifulSoup(html_txt, 'html.parser')

        name_tag = soup.find('h2', {'class': 'wprm-recipe-name wprm-block-text-bold'})
        recipe_name = name_tag.text

        # ingredients
        ingredient_tag = soup.find_all('li', {'class': 'wprm-recipe-ingredient'})
        txt = ''
        for i in ingredient_tag:
            txt = txt + i.text.strip() + ', '
        ingredients = txt.rstrip(', ')

        # procedure
        procedure_tag = soup.find_all('div', {'class': 'wprm-recipe-instruction-text'})
        txt = ''
        for i in procedure_tag:
            txt = txt + i.text.strip()
        procedure = txt.strip()

        ingredients_procedure_lst.append(ingredients)
        ingredients_procedure_lst.append(procedure)
        recipe_dict[recipe_name] = ingredients_procedure_lst
    except:
        ingredients_procedure_lst = []
        ingredients = ''
        procedure = ''
        recipe_name = ''


    # end
    # now return the recipe_dict dictionary with all the recipes

    return recipe_dict


def test():
    recipe_dict = scrape()
    for i in recipe_dict.keys():
        print(i)


def main():
    # test()
    # print(simple())
    print(course_specific('snack'))
    # print(seasonal())
    # (combined('lunch'))
    lst = []
    # recipe_name = ''
    # while recipe_name != 'isombe':
    #
    #     a = simple()
    #     recipe_name = a.split('\n')[0]
    #     if recipe_name not in lst:
    #         lst.append(recipe_name)
    #     if len(lst) == 8:
    #         break
    # print(lst)


if __name__ == '__main__':
    main()
