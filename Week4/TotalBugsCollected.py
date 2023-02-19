# Write a program that counts number of bugs collected over five days
#  Return total to the user

# Prepare vars
numOfDays = 0
numOfBugs = 0

# Count number of bugs over five days
while numOfDays < 5:
    numOfBugs += int(input(f'How many bugs were collected on day {numOfDays+1}? '))
    numOfDays += 1

print(f"The total number of bugs collected over {numOfDays} days is {numOfBugs}")