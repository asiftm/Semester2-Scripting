import numpy as np

# file = open('data.csv').read().replace('year,month,date_of_month,day_of_week,births,date\n','').replace('\n,,,,,','').split('\n')
# file.pop(len(file)-1)
# list_array = []
# for i in file:
#     temp=[]
#     for j in i.split(','):
#         if '/' not in j:
#             temp.append(j)
#     list_array.append(temp)
# arr = np.array(list_array,dtype='i')
#
# print(arr)

arr = np.loadtxt('data.csv',dtype='U',delimiter=',')
arr = arr[1:]
print(arr[:])
