from bs4 import BeautifulSoup
import requests


def explain(text):
    url = 'https://spaceplace.nasa.gov/glossary/en/'
    r = requests.get(url)
    txt_code = r.text
    soup = BeautifulSoup(txt_code, 'html.parser')
    tag_lst = soup.find_all('p')

    for i in range(len(tag_lst)):
        try:
            if (tag_lst[i].getText().split(':')[0]) == text.capitalize():
                print(tag_lst[i].getText().split(':')[1].strip())
                return
        except:
            continue
    print('No definition found!')


def related(text):
    url = f'https://relatedwords.io/{text}'
    r = requests.get(url)
    txt_code = r.text
    soup = BeautifulSoup(txt_code, 'html.parser')
    tag_lst = soup.find_all('span', {'class': 'term'})
    try:
        for i in range(5):
            print(tag_lst[i].text.strip())
    except:
        print('No related terms!')


def coloring(text):
    url = f'https://www.ultracoloringpages.com/s/{text.lower()}-coloring-pages'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    img = soup.findAll('div', {'class': 'page-thumb'})
    if len(img) == 0:
        print('Failed to download image!')
        return
    for i in img:
        try:
            lst1 = str(i).split('\n')
            lst2 = lst1[1].split('"')
            name = lst2[1].split(' ')[0]
            img_url = lst2[3]
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                with open(f'{text}.png', 'wb') as f:
                    f.write(img_response.content)
                print(f'Downloaded {name}.png')
            else:
                print('Failed to download image!')
            break
        except:
            print('Failed to download image!')


def book(text):
    url = 'https://childhood101.com/space-books-for-kids/'
    r = requests.get(url)
    txt_code = r.text
    soup = BeautifulSoup(txt_code, 'html.parser')
    tag_lst = soup.find_all('td')
    lst = []
    for i in range(len(tag_lst)):
        lst.append(tag_lst[i].text.split('\n')[0].strip())

    for i in lst:
        if text.lower() in i.lower():
            print(i)
            return
    print('No book found!')


def extra():
    print('')


def main():
    input_text = input().strip()
    explain(input_text)
    related(input_text)
    coloring(input_text)
    book(input_text)


if __name__ == '__main__':
    main()
