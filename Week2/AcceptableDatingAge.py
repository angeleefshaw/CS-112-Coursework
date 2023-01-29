# Problem 1 : Acceptable Dating Age Calculator 
age = input('Enter your age ')
name = input('Enter your name ')

youngestDatableAge = (int(age)/2) + 7

# Examples ...
# 18 - 16->22  -- lower bound 2 - upper bound 4
# 30 - 22->46  -- lower bound 8 - upper bound 16

# double the lower bound and add it to current age?

oldestDatableAge = ((int(age) - youngestDatableAge)*2) + int(age)

print(f'You can date people as young as {youngestDatableAge}')
print(f'You can date people as old as {oldestDatableAge}')



 