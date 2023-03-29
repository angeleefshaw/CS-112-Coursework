# Add code to a guessing game to show users guesses that have already been made
import random

def main():
    correctNum= random.randint(1,20)
    usersGuess = 0
    guesses = []
    
    while usersGuess != correctNum:
        usersGuess = int(input('Guess a number between 1 and 20 \n'))

        if(usersGuess != correctNum):
            guesses = handleGuesses(guesses, usersGuess)
        else:
            print('Congratulations! You guessed the number!')

def handleGuesses(guesses, guess): 
    if guess in guesses: 
        print('That number has already been guessed!')
    else:
        print('Incorrect. Guess again...')
        guesses.append(guess)

    return guesses


main()


