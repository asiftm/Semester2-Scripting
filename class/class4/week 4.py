'''my_firs t_name = 'asif'
my_last_name = 'mahmud'
my_full_name = my_first_name + ' ' + my_last_name
print(my_full_name)

a= len((my_full_name))
print(type(a))'''



from datetime import datetime

birthday = '02-08-2000'
current_date=datetime.now()

birthday_date =datetime.strptime(birthday,'%d-%m-%Y')
age = current_date-birthday_date
print(age.days)
