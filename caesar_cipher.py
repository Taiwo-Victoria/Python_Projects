#                   ENCRYPTION AND DECRYPTION USING CAESAR CIPHER METHOD

# Taking the user message for encryption of decryption
print('\n Welcome!!! \n')
print('You can either encrypt or decrypt a message, provided you have the password key !!!\n')

user_message = input('Enter your message: ')
password = int(input('Enter your password key (must be an integer): '))

# defining the function for encrypting
def cipher(message, key):

    output = ''

    key = password % 26
    # using ascii code for encryption
    for character in message:
        if character.isalpha(): # checking if it is an alphabet
            code = ord(character) # storing the ascii code of the character as the code
            encrypt = code + key # performing the shifting
            new_code = chr(encrypt) # changing from ascii code to alphabet letter
            output += new_code  #saving the characters 
        else:
            output += character # keeping the symbols as it is
    return output

def decrypt(message, key):
    
    output = ''

    key = password % 26
    # using ascii code for encryption
    for character in message:
        if character.isalpha(): # checking if it is alphabet
            value = ord(character) # storing the ascii code of the character as the code
            decrypt = value - key # performing the decryption by shifting back the character to its original number
            new_value = chr(decrypt) 
            output += new_value
        else:
            output += character
    return output

choice = input('What will you like to do?(encrypt / decrypt): ').lower()
if choice == 'encrypt':
    Encryption = cipher(user_message, password)
    print(f'This is your Ecrypted Text: {Encryption}')
    
elif choice == 'decrypt':
    Decryption = decrypt(user_message, password)
    print(f'This is your Original Text: {Decryption}')
    
else:
    print('Pick a valid option')