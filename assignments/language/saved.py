import requests
import json


def language(text):
    try:
        url = "https://text-analysis12.p.rapidapi.com/language-detection/api/v1.1"
        payload = {
            "text": text
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "9a81a971b3msh34cb1c391aed569p10a071jsnf95a632ba13e",
            "X-RapidAPI-Host": "text-analysis12.p.rapidapi.com"
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        json_data = json.loads(response.text)

        lan = list(json_data["language_probability"])[0]

        txt = open('iso_639_1codes.csv').read().split('\n')
        for i in txt:
            if i.startswith(lan):
                return i.split(',')[1].strip()

    except:
        return 'Something went wrong with the language detection!'


def stopwords(text, language):
    try:
        txt_file_lst = open(f'{language.lower()}.txt').read().replace('\n', ' ').split(' ')
        text_lst = text.lower().replace(',','').replace('.','').replace('!','').replace('?','').split(' ')

        count = 0
        for i in text_lst:
            if i in txt_file_lst:
                count += 1

        return count
    except:
        return 0


def countries(language):
    import requests
    import json

    response = requests.get(f"https://restcountries.com/v3.1/all")
    json_data = json.loads(response.text)
    lst = []
    for i in json_data:
        try:
            for j in i["languages"].values():
                if language in j:
                    lst.append(i['name']['common'])
        except:
            continue

    return sorted(lst)


def sentiment(text):
    import requests
    import json

    url = "https://multilingual-sentiment-classifier.p.rapidapi.com/ml/sentiment-class/"
    payload = {"texts": [f"{text}"]}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "9a81a971b3msh34cb1c391aed569p10a071jsnf95a632ba13e",
        "X-RapidAPI-Host": "multilingual-sentiment-classifier.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    json_data = json.loads(response.text)

    return (json_data['results'])[0]['label']


def population(country):
    import requests
    import json

    response = requests.get(f"https://restcountries.com/v3.1/name/{country}?fullText=true")
    json_data = json.loads(response.text)
    return (json_data[0])['population']


def main():
    input_text = input().lower()

    language_name = language(input_text)
    if language_name=='Something went wrong with the language detection!':
        print(language_name)
        exit()

    print(f'The detected language is {language_name}')

    print(f"{stopwords(input_text, language_name)} stopwords found")

    print(f'The text is {sentiment(input_text)}')

    country_lst = countries(language_name)
    country_population_dict = {}
    for i in country_lst:
        country_population_dict[i] = population(i)
    sorted_populations = dict(sorted(country_population_dict.items(), key=lambda item: item[1], reverse=-1))
    print(f'The majority of people who speak {language_name} live in {next(iter(sorted_populations))}')


if __name__ == '__main__':
    main()