# Create a program that calculates weight loss if a moderately 
# active person cuts their calorie intake by 500 calories/day
# This would result in 4lbs lost a month.

# Collect user starting weightand calculate what their expected weight
# will be at the end of each month for a total of six months.

clientsWeight = input('How much do you currently weigh in pounds? ')
startingWeight = int(clientsWeight)
totalMonths = 6

for x in range(totalMonths):
    clientsWeight = int(clientsWeight) - 4
    print(f'You weight after {x+1} months is {clientsWeight}')

print(f"After {totalMonths} months you can expect to lose {startingWeight - clientsWeight} pounds!")