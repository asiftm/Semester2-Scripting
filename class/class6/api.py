import json
import pandas

# string JSON example
# json_string = '{ "name":"Jason Statham", "age":54, "city":"Chesterfield"}'
# json_dict = json.loads(json_string)
# print(json_dict)
# print(json_dict["age"]) # result is dictionary!


# file = open('jason.json').read()
# json_dict = json.loads(file)
# print(json_dict)


# file = open('jason.json')
# json_dict = json.load(file)
# print(json_dict)

# print(json_dict['people'])
# print(json_dict['people'][1])
# print(json_dict['people'][1]["name"])

# for person in json_dict["people"]:
#     print(f'{person["name"]} is {person["age"]} years old.')

# import requests
# import json
#
# response = requests.get("https://api.kanye.rest/")
# print(response.status_code)
# print(response.headers)
# print(response.text)
# print(response.json)
#
# json_data = json.loads(response.text)
# print(json_data["quote"])


# import requests
# import json
#
# api_url = "https://love-calculator.p.rapidapi.com/getPercentage"
# api_headers = {
#     "x-rapidapi-key": "9a81a971b3msh34cb1c391aed569p10a071jsnf95a632ba13e",
#     "x-rapidapi-host": "love-calculator.p.rapidapi.com"}
# api_query = {
#     "fname": "Elke",
#     "sname": "Christophe"}
#
# response = requests.get(api_url, headers=api_headers, params=api_query)
# print(response.url)
# print(response.text)
# json_data = json.loads(response.text)
# print(json_data["result"])


# import requests
# import json
#
# url = "https://text-analysis12.p.rapidapi.com/language-detection/api/v1.1"
#
# payload = {"text": "Ik ben echt ontzettend teleurgesteld en boos met de slechte kwaliteit die ik heb ontvangen van de klantenservice!"}
# headers = {
# 	"content-type": "application/json",
# 	"X-RapidAPI-Key": "9a81a971b3msh34cb1c391aed569p10a071jsnf95a632ba13e",
# 	"X-RapidAPI-Host": "text-analysis12.p.rapidapi.com"
# }
#
# response = requests.request("POST", url, json=payload, headers=headers)
#
# json_data = json.loads(response.text)
# print(list(json_data["language_probability"])[0])
# print(response.text)


# import requests
# import json
#
# response = requests.get("https://restcountries.com/v3.1/lang/english")
# json_data = json.loads(response.text)
# lst=[]
# for i in json_data:
# 	lst.append((i['name']['common']))
# print(sorted(lst))






# import requests
#
# url = "https://multilingual-sentiment-classifier.p.rapidapi.com/ml/sentiment-class/"
#
# payload = {"texts": ["Ми живемо в прекрасному світі з багатою культурою та чудовими людьми!"]}
# headers = {
# 	"content-type": "application/json",
# 	"X-RapidAPI-Key": "9a81a971b3msh34cb1c391aed569p10a071jsnf95a632ba13e",
# 	"X-RapidAPI-Host": "multilingual-sentiment-classifier.p.rapidapi.com"
# }
#
# response = requests.request("POST", url, json=payload, headers=headers)
#
# print(response.text)