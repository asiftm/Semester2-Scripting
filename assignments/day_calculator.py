
import datetime
import calendar

date_input = input('What is your birthday? ')

date_object = datetime.date.fromisoformat(date_input)
weekday_num = date_object.weekday()
weekday_name = calendar.day_name[weekday_num]

print(weekday_name)

