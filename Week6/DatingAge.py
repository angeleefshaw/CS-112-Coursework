def main():
    introduction()

    clientsAge = int(input('What is your age? \n'))
    poiAge = int(input('What is the age of your person? \n'))

    return shouldYouDate(poiAge, ageLowerLimit(clientsAge), ageUpperLimit(clientsAge))

def introduction():
    print('This program is designed to help you identify prospective matches within an ideal age range.')

def ageUpperLimit(clientsAge):
    return (clientsAge - 7)*2

def ageLowerLimit(clientsAge):
    return (clientsAge/2) + 7

def shouldYouDate(poiAge, lowerLimit, upperLimit):
    if(poiAge >= lowerLimit and poiAge <= upperLimit):
        print('You can date!')
        return True
    else: 
        print('You should not date.')
        return False
    
main()