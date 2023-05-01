# import language as lg
# output= lg.language("Azi am mers la piață să cumpăr legume proaspete.")
# print(output)


# import language as lg
# output = lg.stopwords("ليس هناك أي شيء يمكنني القيام به في هذا الوقت لأنني لا أملك أي موعد، وأنا لست متأكدًا مما إذا كنت سأتمكن من العثور على أي شيء آخر لأفعله، ولكني سأجلس هنا في هذا المكان لبعض الوقت على الأقل","arabic")
# print(output)

import requests
import json
response = requests.get(f"https://restcountries.com/v3.1/all")
json_data = json.loads(response.text)

language = 'Norwegian'
lst=[]
for i in json_data:
    try:
        for j in i["languages"].values():
            if language in j:
                lst.append(i['name']['common'])
    except:
        continue

print(lst)

