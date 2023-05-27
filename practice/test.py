import json

import requests

url = "https://joj-image-search.p.rapidapi.com/v2/"

querystring = {"q": "cow", "hl": "en"}

headers = {
    "X-RapidAPI-Key": "9a81a971b3msh34cb1c391aed569p10a071jsnf95a632ba13e",
    "X-RapidAPI-Host": "joj-image-search.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

json_data = json.loads(response.text)

img_link = (json_data['response']['images'][0]['image']['url'])
