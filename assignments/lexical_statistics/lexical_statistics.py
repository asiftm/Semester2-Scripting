text = open('sonnets.txt').read().split()

input_lst = []
for i in text:
    input_lst.append(
        i.replace(',', '').replace(':', '').replace('‘', '').replace('.', '').replace('!', '').replace('?', '').lower())

sorted_lst = sorted(input_lst)
unique_lst = list(dict.fromkeys(sorted_lst))

thisdict = {}

for i in range(len(unique_lst)):
    count = 0
    for j in range(len(sorted_lst)):
        if unique_lst[i] == sorted_lst[j]:
            count += 1
    thisdict[count] = unique_lst[i]

countlst = thisdict.keys()
countlst = sorted(countlst)
countlst.reverse()

print('The 50 most common words by Shakespeare:')
for i in range(50):
    print(thisdict[countlst[i]], countlst[i])
