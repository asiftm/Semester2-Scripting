""""#one line comment

print("hi") #comment in the same line with code
print("hi","hey" +'hello') # , and + can be used in print(), a , adds a space but a + dont add space
print(3+2)

#variables and their outputs
#variables names are case sensitive
string = "a"
print(string)
string2 = 'b'
print(string+string2)
int = 3
print(int)
print(string+str(int))
float = 5.0
print(float)
king=boss=sir='asif' #many variables with the same name
print(king,boss,sir)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits #unpack a list
print(x)
print(y)
print(z)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a) #multiple line string

#getting the type of a variable
print(type(string))
print(type(int))
print(type(float))

#type casting
number = 5

print(type(str(number)))
#getting a random number
import random
print(random.randrange(1, 10))
"""
import os
import pathlib

'''
     0
    000
   00000
  0000000
 000000000
00000000000

a = 6
b=11
box=''
space=''
total=''
for i in range(0,b):
    box = ''
    space = ''
    if(i%2==0):
        for j in range(0,i+1):
            space=''
            for k in range(int(i/2),int((b-1)/2)):
                space+=(' ')
            box+=str(0)
    total = space + box
    print(total)

'''


# for i in range(2000,10000):
#     print(i,chr(i))


# calculator = pathlib.Path("C:\Windows/System32/calc.exe")
# print("Filename:", calculator.name)
# print("Name:", calculator.stem)
# print("Extension:", calculator.suffix)
# print("Parent directory:", calculator.parent)
# print("Is file?", calculator.is_file())
# print("Is dir?", calculator.is_dir())
# print("File Exists?", calculator.exists())


from pathlib import Path
# print(str(Path.home()) + "\\" + "test") #windows
# print(str(Path.home()) + "/" + "test")  #linux/macOs
# print(Path.home() / "test")


# file_ = open('bacon.txt', 'w')
# file_.write('Hello, world!\n')
# file_.close()
# file_ = open('bacon.txt', 'a')
# file_.write('Bacon is not a vegetable.')
# file_.close()
# for f in os.listdir():
#     print(f)


# file_ = open('bacon.txt', 'r')
# print(file_.read())
# file_.close()
#
# file_ = open('bacon.txt', 'r')
# print(file_.read(10))
# file_.close()
#
# file_ = open('bacon.txt', 'r')
# print(file_.readlines())
# file_.close()













