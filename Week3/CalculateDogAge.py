# Calculate dog age given years and weight of dog

# All dogs 
# year 1 = 15YO
# year 2 = 21YO

# Collect Data
years = input('How many years has your dog be alive? ')
weight = input('What is the weight of your dog in pounds? ')

age = 0

if int(years) == 1:
    print("Your dog's age in human years is 15")
    exit()
elif int(years) == 2:
    print("Your dog's age in human years is 21")
    exit()
elif int(years) > 30:
    print('The years enetered is out of range. Please try again')
    exit()
elif int(years) > 2:
    age = 21

iteration = int(years) - 2

for x in range(iteration):
    if int(weight) < 20 :
        age = age + 4
    elif int(weight) >= 20 and int(weight) < 50 :
        age = age + 5
    elif int(weight) >= 51 and int(weight) < 90 :
        age = age + 6
    elif int(weight) >= 90 :
        age = age + 7
    else :
        print('The year amount you entered is out of range')


print(age)

# Need to run a loop for every year after 2
# Increment age for every iteration of loop


# if weight < 20
# age = age + 4
# if weight >= 20 or < 50
# age = age + 5
# if weight >= 51 or < 90
# age = age + 6
# if weight > 90
# age = age + 7
# else
# print('The year amount you entered is out of range')


# Dog 1 - 12 yrs & 20lbs - 71 years old in human years
# Dog 2 - 8 years & 90lbs - 63 years old in human years
# Dog 3 - 2 years & 77lbs - 21 years old in human years

