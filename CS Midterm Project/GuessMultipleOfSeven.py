import random

# Program that allows two players to guess a number from 1-100 that is a multiple of seven.
# EXTRA - Allow 3 games to be played in total

# Inlcude a main function gives game instructions to users
    # Collect names of 2 players
    # Altername players and call by name when it is their turn
    # Each player gets 3 guesses until the number has been guessed and a winner is declared
def main():
    multiple = getMultiple()
    correctNum = getCorrectNum(multiple)
    totalTurns = 6

    instructions(multiple)

    player1 = input('Enter the name of the first player \n')
    player2 = input('Enter the name of the second player \n')


# Prints game instructions to the console
# EXTRA - Adapt instructions to inform user of the new multiple for each new game
def instructions(multiple):
    print(f'Welcome to the guessing game! Two players will have three turns each to guess a number between 1 and 100. This number must be a mulitple of {multiple}')

# Get the games multiple
def getMultiple():
    # Returns a random multiple (not 1 because thats not helpful)
    return random.randint(2,9)

# Function to select random number that is multiple of 7 and between 1-100
# EXTRA - for each new game, allow the multiple to change (5,8,9 ect.)
def getCorrectNum(multiple):
    factor = 100/multiple
    divider = random.randint(1, int(factor))

    # Returns a number
    return (multiple*divider)


# Is users input a multiple of multiple?
def isGuessValid(num, multiple):
    print('Checks user input for multiple of 7 validity')
    # returns either true or false


# Check to see if user input is too high or too low
def getGuessRange(num, correctNum): 
    if(num < correctNum):
        print('Guess is too low')
    elif (num > correctNum):
        print('Guess is too high')


# Final function to announce winner or losers
def announceVictor(userName):
    print('Congratulate the winner by name or that they are losers')


# EXTRA - get player stats and congratulate the player who wins the most games
def getPlayerStats():
    print('Congratulations Player1, you have won x games in total!')

main()