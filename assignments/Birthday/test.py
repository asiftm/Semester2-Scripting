import numpy as np

file = open('data.csv').read().replace('year,month,date_of_month,day_of_week,births,date\n','').replace('\n,,,,,','').split('\n')
arr = np.array(file)

print(arr)