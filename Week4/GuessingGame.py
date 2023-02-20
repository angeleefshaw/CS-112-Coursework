# Give a user three guesses in a programmatic guessing game

# Set vars
numOfGuesses = 3
solution = 3

# Allow user to guess and exit if answer is correct
for i in range(numOfGuesses):
    userGuess = input('Guess a number between 1 and 10 ')

    if(int(userGuess) == solution):
        print('Thats correct!')
        exit()
    else: 
        print('Incorrect! Try again ')

# Input - 2 will yeild 'Incorrect!...'
# Input - 3 will yeild 'Correct...'