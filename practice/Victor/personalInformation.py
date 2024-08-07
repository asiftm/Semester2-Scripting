import threading
import requests
import json
from PIL import Image, ImageDraw, ImageFont

def API():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    json_data = json.loads(response.text)
    print(json_data)


def main():
    API()


if __name__ == "__main__":
    main()