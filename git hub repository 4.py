##saving the accounts and the passwords....

import pyperclip
password={
    'snap':'abc@123',
    'gmail':'likhi@123',
    'insta':'ghi@123',
    }
account=input('enter the account name: ')
if account in password:
    pyperclip.copy(password[account])
    print('password copied to clipboard')
else:
    print('password not found')
