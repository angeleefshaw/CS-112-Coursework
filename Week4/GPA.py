# Collect letter grades from user and return their GPA for a given semester

# Prepare predefined vars
courseCount = 3
acceptableGrades = ['a', 'b', 'c', 'd', 'f']
i = 0
total = 0.0

# For each course, ask user for their letter grade and add to total
while i < courseCount:
    grade = input(f'Enter the letter grade for course {i+1} ').lower()

    if grade in acceptableGrades:
        if(grade == 'a'):
            total = float(total + 4.0)
        elif(grade == 'b'):
            total = float(total + 3.0)
        elif(grade == 'c'):
            total = float(total + 2.0)
        elif(grade == 'd'):
            total = float(total + 1.0)
        else:
            total = float(total + 0.0)
        
        i += 1
    else:
        print('Please enter an accepatable letter grade ')

print(f'Your GPA is {round((total/courseCount), 2)}')

# Input - b,b,b will yeild 3.0 GPA
# Input - a, b, c will yeild 3.0 GPA


