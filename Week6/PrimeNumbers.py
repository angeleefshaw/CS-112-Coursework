# Write a program that determines if a number is prime
# and returns true or false

setOfPrime = [3,5,7]

# Could be better.. quick and dirty

# Check if divisible by 2, otherwise check all
# numbers greater than 7 for divisibility by primary 
# prime numbers

def isPrime(num) :
    if((num/2).is_integer()):
        return False
    elif(num > 7):
        for i in (setOfPrime):
            if((num/i).is_integer()):
                return False
        return True
    else:
        return True

   
def checkPrime():
    num = int(input('Enter a number you would like to check \n'))

    if(isPrime(num)):
        print(f'{num} is prime')
    else:
        print(f'{num} is not prime')

checkPrime()