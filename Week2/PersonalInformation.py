# Write a program that collects personal information from users
# Name
# Address
# Telephone Number
# College Major

print('Help me get to know you. Answer the questions below...')

name = input('Enter your name ')
address = input('Enter your address (please include city, state and zipcode)')
phoneNumber = input('Enter your phone number')
collegeMajor = input('Enter your college major')

print('')
print(f'Nice to meet you {name}')
print(f'I see you live at {address}')
print(f'I can reach you at {phoneNumber}')
print(f"I see you're currently studying {collegeMajor}")
