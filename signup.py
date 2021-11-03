username = input('Insert username: ')
valid_password = False

while valid_password == False:
    password = input('Insert a password: ')
    password_confirm = input('Confirm your password: ')

    if password == password_confirm:
        valid_password = True
        print(f'{username}, you have sucessfully signed up! :)')
    else:
        print('The passwords do not match :(\nPlease try again')
