password=input('Your password:')
#basic condition checks
password12345=password.find('12345')
password_password=password.find('password')
qwerty=password.startswith('qwerty')
non_alphabetic =False
non_digit=False
for i in password:
    if i.isalpha():
        non_digit=True
    else:
        non_alphabetic=True
special_character_one = password.find('@')
special_character_two=password.find('$')
special_character_three=password.find('!')
upper = False
lower = False
for j in password:
    if j.isupper():
        upper = True
    elif j.islower():
        lower = True
#conditions
if password12345<0 and password_password<0:
    if qwerty==False:
        if non_alphabetic ==True:
            if non_digit==True:
                if special_character_one>0 or special_character_two>0 or special_character_three>0:
                    if upper==True and lower == True:
                        print("\nThe password is valid!")
                    else:
                        print('\nThe password must have both uppercase and lowercase letters.')
                else:
                    print('\nThe password must contain at least one of the following special characters: $, @ or !.')
            else:
                print('\nThe password must contain at least one non-digit character.')
        else:
            print('\nThe password must contain at least one non-alphabetic character.')
    else:
        print('\nThe password may not start with the keyword “qwerty” but it may contain it.')
else:
    print('\nThe password may not contain the keywords “password” or “123456”.')