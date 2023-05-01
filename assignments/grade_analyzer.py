import math

input_digit = input('input: ')
num_list = []

if input_digit.isdigit():
    while input_digit.isdigit():
        num_list.append(int(input_digit))
        input_digit= input('input: ')

#minimum_value
    minimum = min(num_list)
    print(f'Minimum:  {minimum}')
#maximum_value
    maximum = max(num_list)
    print(f'Maximum:  {maximum}')
#average_value
    average = sum(num_list)/len(num_list)
    print(f'Average:  {average}')
#standard_deviation
    square_sum = 0
    for i in num_list:
        difference = (i - average)**2
        square_sum += difference
    variance = square_sum/len(num_list)
    standard_deviation = math.sqrt(variance)
    print(f'SD:  {standard_deviation}')
else:
    print('No integer given.')  