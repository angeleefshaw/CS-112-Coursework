# Write a program that calculates a total salary if salaray increased
# by one penny a day for x number of days

totalDays =int(input('How many days of pay would you like to calculate? '))
salary = 0

# Loop through amount of days and calculate
for x in range(totalDays):
    salary += 1

print(f"Your total salary after {totalDays} days is {round(salary/100, 2)}")

# Input - 20 days yeilds 0.20 cents 
# Input - 130 days yeilds 1.30 cents
