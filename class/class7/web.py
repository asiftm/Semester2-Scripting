from bs4 import BeautifulSoup
import requests


url = 'https://en.wikipedia.org/wiki/Sea_Peoples'
r = requests.get(url)

soup = BeautifulSoup(r.text)

result = soup.find_all('img')
for i in result:

    a = (i.get('src'))


