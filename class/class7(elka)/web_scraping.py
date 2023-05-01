from bs4 import BeautifulSoup
import requests
import re

# url = 'https://en.wikipedia.org/wiki/Elephant'
# response = requests.get(url)
# html = response.text

# # my way
# print(html.lower().count('elephant'))
# # regex way
# x='(e|E)lephant'
# matches = re.findall(x,html)
# print(len(matches))

# soup = BeautifulSoup(response.text,'html.parser')

# print(soup.prettify())
# print(soup.title)
# print(soup.title.get_text())

# h3_tags = (soup.find_all('h3'))
# for i in h3_tags:
#     print(i.get_text())

# lan_tag = soup.find_all('a',{'class':'interlanguage-link-target'})
# for tag in lan_tag:
#     print(tag['title'])


url = 'https://www.tomorrowland.com/en/festival/line-up/stages/friday-21-july-2023'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html,'html.parser')

tags = soup.find_all('div', {'class': 'stage'})


lst = []
for i in tags:
    lst.append(i.text.strip().replace('\n',''))

for i in lst:
    if i.startswith('Mainstage'):
        lst2 = i.split('  ')
        lst3=[]
        for j in lst2:
            if j != '' and j != 'Mainstage':
                print(j)
        break


# url = 'https://www.tomorrowland.com/en/festival/line-up/stages/friday-21-july-2023'
# response = requests.get(url)
# html = response.text
# soup = BeautifulSoup(html,'html.parser')
#
# tags = soup.find_all('div', {'class': 'stage'})
#
#
# lst = []
# for i in tags:
#     lst.append(i.text.strip().replace('\n',''))
#
# for i in lst:
#     if i.startswith('Mainstage'):
#         lst2 = i.split('  ')
#         lst3=[]
#         for j in lst2:
#             if j != '' and j != 'Mainstage':
#                 print(j)
#         break


print("iiii")


