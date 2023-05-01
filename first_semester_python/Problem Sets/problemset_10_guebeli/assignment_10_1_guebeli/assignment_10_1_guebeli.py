
import re


def find_urls(string):
    regex = r"((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)"
    urls = re.findall(regex, string)
    return [url[0] for url in urls if url[0].startswith("http")]


def import_text(path):
    try:
        f = open(path, "r")
        return f.read()
    except IOError:
        print("File not accessible!")
    finally:
        f.close()


def save_lines(data, file):
    f = open(file, "w")
    text = ""
    for line in data:
        text += line+"\n"

    f.write(text)


if __name__ == '__main__':
    url_list = find_urls(import_text("Python.org.html"))
    url_list = list(dict.fromkeys(url_list))
    save_lines(url_list, "urls.txt")
