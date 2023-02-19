# Write a program that calculates a total salary if salaray increased
# by one penny a day for x number of days

totalDays =int(input('How many days of pay would you like to calculate? '))
salary = 0

for x in range(totalDays):
    salary += 1

print(f"Your total salary after {totalDays} days is {salary/100}")