# Run a loop that takes in a series of positive
# numbers. If a user should enter a negative number,
# end the loop and return the sum of all numbers

# Prepare vars
num = 0
total = 0

# Run so long as num is positive
while num >= 0 :
    enteredNum = int(input('Enter a positive number'))
    num = enteredNum

    if(num >= 0):
        total += enteredNum

print(total)