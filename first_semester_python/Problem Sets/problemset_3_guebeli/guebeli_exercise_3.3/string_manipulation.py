# author: Paolo Gübeli
# version: 28.09.2020

import string

# I define the main.
if __name__ == '__main__':

    # I ask for some text.
    text = input("Insert some text: ")

    # I capitalize the words.
    print(string.capwords(text.strip()))




