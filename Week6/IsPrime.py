def isPrime(num) :
    setOfPrime = [3,5,7]
    
    if((num/2).is_integer()):
        return False
    elif(num > 7):
        for i in (setOfPrime):
            if((num/i).is_integer()):
                return False
        return True
    else:
        return True