for i in range(1,1000):
    print(i)
    print(f"we are printing out a number for the  {i+1}th time")
    print(f"asif is awesome (x{i+1})")

number = 5
for i in range(0,10):
    print(f"{number}*{i+1} = {number * (i+1)}")

name = "asif"
box = ""
for i in name:
    box = box+i
    print(box)

hidden_number = "5"
guess = input("guess the number : ")
while guess != hidden_number :
    print("wrong, guess again")
    guess = input("guess the number : ")
print("you are correct")





