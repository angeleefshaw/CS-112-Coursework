# Write a program that detects the day of the week based off user input

number = input('Enter a number 1-7 ')


if(int(number) >= 1 and int(number)<= 7):
    # Find day of week
    if (number == '1'):
        print('Its Monday!')
    elif (number == '2'):
        print('Its Tuesday!')
    elif (number == '3'):
        print('Its Wednesday!')
    elif(number == '4'):
        print('Its Thursday!')
    elif(number == '5'):
        print('Its Friday!')
    elif(number == '6'):
        print('Its Saturday!')
    elif(number == '7'):
        print('Its Sunday!')
else:
    print(f'ERROR: {number} is not in range')