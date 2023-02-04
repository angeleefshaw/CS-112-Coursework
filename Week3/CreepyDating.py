# Program Goal: program that provides guidance on whether your specific client should date a
# specific other person.

# Client's data
age = input('Enter your age ')
name = input('Enter your name ')

# Client's person of interest data
candidateAge = input('Enter the age of the person you would like to date ')
candidateName = input('Enter the name of the person you would like to date ')

# Find yougest datable age
youngestDatableAge = (int(age)/2) + 7

# Find oldest datable age
oldestDatableAge = (int(age) - 7)*2

# Perform some computations.. no Davids!
if (candidateName.lower() == 'david'):
    print('You cannot date a boy named David')
    exit()
elif (int(candidateAge) >= youngestDatableAge and int(candidateAge) <= oldestDatableAge):
    print(f'Congratulations! You can date {candidateName}')
else:
    print(f'It is creepy to date {candidateName}')
