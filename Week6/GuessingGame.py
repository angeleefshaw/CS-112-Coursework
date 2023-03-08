# Implement a guessing game with one player and 3 max guesses
import random

def main():
    instructions()

    answer = random.randint(1, 10)
    playerName = 'Jean'
    maxGuesses = 3
    guess = -1

    while guess != answer and maxGuesses > 0:
        guess = int(input('Guess a number between 1 and 10!'))
        checkValidInput(guess)
        maxGuesses = maxGuesses - 1

    if(guess == answer):
        print(f'You win! The number was {answer}')
        return
    else: 
        print(f"You did not guess the number. The number was {answer}")
        return

def checkValidInput(input):
    if(input < 1 or input > 10):
        print('Number is not in range')
      
    
def giveHint(guess, answer):
    if(guess > answer):
        print("Your guess is to high")
    else:
        print("Your guess is too low")


def instructions():
    print('Welcome to our guessing game. You will be asked to guess a number between 1 and 10')

main()