print('Enter Password')
password = input()
if len(password) < 8:
    print('Password should have at least 8 characters')
capscheck = any(char.isupper() for char in password)
if capscheck is False:
    print('Password should have at least one uppercase letter')
intcheck = any(char.isdigit() for char in password)
if intcheck is False:
    print ('Password should have at least one number')
if len(password) >= 8 and capscheck is True and intcheck is True:
    print('Valid Password')