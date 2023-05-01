capitals = ["Amsterdam", "Tokyo", "London", "Cape Town"]

#1
print(capitals)
#2
print(capitals[0])
#3
capitals.append('Paris')
print(capitals)
#4
range = capitals[1:3]
print(range)
#5
capitals.reverse()
print(capitals)
#6
capitals.append('Cape Town')
print(capitals)
#7
count = capitals.count('Cape Town')
print(count)
#8
capitals.remove('Cape Town')
print(capitals)
#9
length = len(capitals)
print(length)
#10
capitals.insert(0,100)
print(capitals)
#11
capitals[0] = 'Washington'
print(capitals)