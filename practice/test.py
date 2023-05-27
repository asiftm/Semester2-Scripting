# import json
#
# import requests
#
#
#
# url = "https://joj-image-search.p.rapidapi.com/v2/"
#
# querystring = {"q": "cow", "hl": "en"}
#
# headers = {
#     "X-RapidAPI-Key": "9a81a971b3msh34cb1c391aed569p10a071jsnf95a632ba13e",
#     "X-RapidAPI-Host": "joj-image-search.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# json_data = json.loads(response.text)
#
# img_link = (json_data['response']['images'][0]['image']['url'])
#
# print(img_link)


from PIL import ImageDraw, Image
import requests
import io

image1 = Image.new('RGBA', (1500, 700), 'white')
draw = ImageDraw.Draw(image1)

img_link = 'https://cdn.britannica.com/55/174255-050-526314B6/brown-Guernsey-cow.jpg'
response = requests.get(img_link)
new_image = Image.open(io.BytesIO(response.content))
new_size = (800, 600)
new_image = new_image.resize(new_size)

image1.paste(new_image,(0,0))

image1.save('image1.pdf')
