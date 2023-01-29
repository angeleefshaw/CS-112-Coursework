# Problem 2 - Convert some number of minutes to hours and minutes.

#Example (taken from worksheet) 137 minutes is 1hr and 17mins !! Not correct !!

# How many times does 60 go into minutes? -> this is the value of hours
# What remains? -> this is the value of minutes

minutes = input('Enter the amount of minutes you would like to convert into hours ')

hours = int(minutes)//60
remainingMinutes = int(minutes)%60

print(f'{minutes} minutes is {hours} hours and {remainingMinutes} minutes')