# from bs4 import BeautifulSoup
# import requests
#
# url = 'https://en.wikipedia.org/wiki/Soup'
# r = requests.get(url)
# txt = r.text
# soup = BeautifulSoup(txt)
#
# print(soup.title)
# print(soup.title.get_text())
# print(len(soup.get_text()))
# print(soup.get_text()[0:500].split())
# print(soup.get_text().count("soup"))


from bs4 import BeautifulSoup
import requests
#
# txt = input()

url = f'https://en.wikipedia.org/wiki/soup'

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

a_tags = soup.find_all('a', {"class": "interlanguage-link-target"})
print(a_tags)

# for i in a_tags:
#     if f'Bangla' in (i['title']):
#         print((i['title']).split(' ')[0])
# # or more pythonic ;)
# names = [a['title'] for a in a_tags]
# print(names)