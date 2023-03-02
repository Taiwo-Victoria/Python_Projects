#         EMAIL SLICER

print('welcome to Email Slicer')
print('')  #printing an empty line

email = input('Kindly Provide your email: ') #accepting the email of the user
print('')

if('@' in email): # checking if the email provided is correct
    username = email[:email.index('@')]  # saving all characters before the @ 
    domain = email[email.index('@')+1:] # saving all characters after the @
    print('The email address that you provide is: ', email) # printing out the email provided
    print('')
    print('The username is: ',username, 'and it domain server is: ', domain) #printing the username and domain gotten from the email provided
   
#notifying the user of incorrect email address entry. 
else: 
    print('Kindly provide a valid email address!!!') 