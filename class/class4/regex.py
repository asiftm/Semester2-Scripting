#practice

# print('This is Alice's cat.') won't work
# print("This is Alice's cat.")
# print('This is Alice\'s cat.')
# print('Mary: "Hello"')
# print("Mary: \"This is Alice's cat.\"")
# print(r"Mary: \"This is Alice's cat.\"")

# string = "This is Alice's cat."
# print(string[1:4])
# print(string[:4])
# print(string[4:])
# print(string[::-1])  #reverse
# print(string[1::2])
# print(string[1::2])
# print("cat" in string)
# print("Cat" not in string)

# string ="Hello my name is 	elke"
# print(string.split())
# print(string.split("e"))
# print(string.split("el"))
# print("-".join(string.split()))

# string = "Testing 1 2 3"
# new_string=""
# sum_string=0
# for c in string:
#     if c.islower():
#         new_string += c.upper()
#     elif c.isupper():
#         new_string += c.lower()
#     elif c.isdigit():
#         sum_string += int(c)
#     elif c.isspace():
#         new_string += "-SPACE-"
# print(new_string)
# print(sum_string)

# string ="   Let's strip this string             ";
# print(string.lstrip())
# print(string.rstrip())
# print(string.strip())

# string = 'Hi\nHello\n'
# print(string)
#
# raw_string = r'Hi\nHello'
# print(raw_string)

# import re
# string = "There are 10 kinds of people, those who understand binary and those who don't! Are you 1 of the 1st group?"
# #finding all digits
# result = re.search(r'\d', string)
# print("First occurence = " + result.group())
# print("Location = " + str(result.span()))
# result = re.findall(r'\d', string)
# print(result)
# #finding all numbers
# result = re.findall(r'\d+', string)
# print(result)
# #many ways to regex
# result = re.findall('[0-9]', string)
# print(result)

# import re
# string = "There are 10 kinds of people, those who understand binary and those who don't! Are you 1 of the 1st group?"
# #finding all digits
# regex_object = re.compile(r'\d')
# result = regex_object.search(string)
# print("First occurence = " + result.group())
# result = regex_object.findall(string)
# print(result)
# result = regex_object.findall("My number is 0456 12 45 78")
# print(result)

# import re
# string = "There are 10 kinds of people,those who understand binary and those who don't! Are you 1 of the 1st group?"
# regex_object = re.compile(r'\d')
# print(regex_object.match(string))
# regex_object = re.compile(r'\d')
# print(regex_object.search(string))

import re
string='''RegExr was created by gskinner.com.

Edit the Expression & Text to see matches. Roll over matches or the expression for details. PCRE & JavaScript flavors of RegEx are supported. Validate your expression with Tests mode.

The side bar includes a Cheatsheet, full Reference, and Help. You can also Save & Share with the Community and view patterns you create or favorite in My Patterns.

Explore results with the Tools below. Replace & List output custom results. Details lists capture groups. Explain describes your expression in plain English.
'''



