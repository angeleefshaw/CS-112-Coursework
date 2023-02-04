# Design a program that promps a user to enter in two primary colors. 
# Display the secondary color that would result from mixing the two colors

color1 = input('Enter a primary color ')
color2 = input('Enter a primary color ')

primaryColors = ['blue', 'red', 'yellow']

colorList = []
colorList += [color1.lower()]
colorList += [color2.lower()]

if (color1.lower() not in primaryColors and color2.lower() not in primaryColors):
    print('Error: Please enter two primary colors')

if('blue' in colorList and 'red' in colorList):
    print('Purple')
elif('blue' in colorList and 'yellow' in colorList):
    print('Green')
elif('yellow' in colorList and 'red' in colorList):
    print('Orange')

