def main():
    age = int(input("What is your dog's age in years? "))

    if age > 40:
        print('The years enetered is out of range. Please enter a valid age. ')
        exit()

    hEqYrs = findHumanEqYears(age)

    print("your dog is equivalent to a " + str(hEqYrs) + " year old human")

    reportAgeRange(hEqYrs); 


def findHumanEqYears(years):
    if years == 1:
        return(15)
    elif years == 2:
        return(21)
    elif years > 2:
        weight = int(input("What is your dog's weight in pounds? "))

        if (weight < 1): 
            print('The weight amount you entered is not possible. Please enter a valid weight.')
            exit()

        multiplier = findMultiplier(weight)

    hEq = ((years - 2)*multiplier + 21)
    return(hEq)


def findMultiplier(weight):
    if int(weight) < 20 :
        multiplier = 4
    elif int(weight) >= 20 and int(weight) < 50 :
        multiplier = 5
    elif int(weight) >= 51 and int(weight) < 90 :
        multiplier = 6
    elif int(weight) >= 90 :
        multiplier = 7

    return(multiplier)

def reportAgeRange(hEq):
    if (hEq < 18):
        print("It looks like your dog is a puppy!")
    elif (hEq >= 18 and hEq < 21):
        print("It looks like your dog is an adolescent.")
    elif (hEq >= 21 and hEq < 65 ):
        print("It looks like your dog is middle-aged.")
    else:
        print("It looks like your dog is old.")

main()    


    
