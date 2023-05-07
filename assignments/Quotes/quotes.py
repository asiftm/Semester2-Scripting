import threading
import requests
import json
from PIL import Image, ImageDraw, ImageFont


def download_images(image_number):
    url = 'https://picsum.photos/200/300'
    response = requests.get(url)
    if response.status_code == 200:
        with open(f'{image_number}.png', 'wb') as f:
            f.write(response.content)
    return f'{image_number}.png'


def quotes():
    url = "https://quotes-by-api-ninjas.p.rapidapi.com/v1/quotes"
    headers = {
        "X-RapidAPI-Key": "9a81a971b3msh34cb1c391aed569p10a071jsnf95a632ba13e",
        "X-RapidAPI-Host": "quotes-by-api-ninjas.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    return json_data[0]['quote']


def quote_on_image(quote, image_name):
    im = Image.open(image_name)
    draw = ImageDraw.Draw(im)

    font_size = 5
    font_color = (255, 255, 255)
    font_path = "arial_bold.ttf"

    font = ImageFont.truetype(font_path, font_size)
    text_position = (10, 200)
    text = quote
    draw.text(text_position, text, font=font, fill=font_color)
    im.save(f'quote_{image_name}')


def all_functions(i):
    image_name = download_images(i)
    quote = quotes()
    quote_on_image(quote, image_name)


def main():
    threads = []
    for i in range(20):
        t = threading.Thread(target=all_functions(i))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
