import pandas as pd
day = 2
month = 5
# df = pd.read_csv("./data.csv")

# birth_total = df['births'].sum()

# day_total = df[(df['month']==month)&(df['date_of_month']==day)]['births'].sum()

# percentage = (day_total*100)/birth_total
# print(round(percentage,2))

df = pd.read_csv("./data.csv")
birth_total = df['births'].sum()
day_total = df[(df['month']==month)&(df['date_of_month']==day)]['births'].sum()
percentage = (day_total*100)/birth_total
print(f'Percentage of people born on same day: {round(percentage,2)} %')
# day_info = df[(df['month'] == month) & (df['date_of_month']==day)]
# day_births = day_info['births'].sum()


# answer = round((day_births * 100)/total_births,2)
# print("Percentage of people born on same day:",answer)