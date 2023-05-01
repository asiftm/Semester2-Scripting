input = input('Your input number: ')

if input.isdigit():
    digit = int(input)
    if digit%2==0:
        print('OK!')
    else:
        print('Error detected!')
else:
    print('Please input a digit.')