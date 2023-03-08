# Use the isPrime function created to print all
# prime numbers in the range of 100 numbers

from IsPrime import isPrime

for i in range(100):
    if(isPrime(i)):
        print(i)