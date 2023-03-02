#                            Python project on Random Password Generator



 
import string
import secrets 

# for all the alphabets including capital and small letters
alpha = string.ascii_letters

# for all digits from 0 to 9
numb = string.digits

# for all special characters
symbols = string.punctuation


print("Welcome to My Random Password Generator")
name = input('What is your name: ')
print('Your password length should be between 12 to 16')
pwd_len = input('Enter the password length you want(12 - 16): ')
print('You will be providing the necessary number of alphabets, numbers, and special character you want in your password')
no_alpha = int(input('How many alphabets do you want: '))
digits = int(input('How many digits do you want: '))
no_sys = int(input('How many special characters do you want: '))

pwd_lenght = no_alpha + digits + no_sys

if pwd_lenght < int(pwd_len):
    print('Kindly enter a password length in the range 12 to 16 ')
else:
    
    pwd_alpha = ''
    for i in range (no_alpha):
        pwd_alpha += ''.join(secrets.choice(alpha))

    pwd_dig = ''
    for i in range(digits):
        pwd_dig += ''.join(secrets.choice(numb))
    
    pwd_sys = ''
    for i in range(no_sys):
        pwd_sys += ''.join(secrets.choice(symbols))        
            
    password = pwd_alpha + pwd_dig + pwd_sys
  
    print(name, 'Your password is: ',password)

