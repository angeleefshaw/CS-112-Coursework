import random

# Program that hosts 3 rounds of a number guessing game. Players must guess a number between 1 and 100. 
# The number must be a multiple of x. This multiple changes each round.
# Gives the stats of the best guesser after all three rounds are complete

def main():
    numOfGames = 3
    player1Wins = 0
    player2Wins = 0

    print('Welcome to the guessing game! We will play three rounds to see which player is the best guesser')
    print('Players must guess a number between 1 and 100.')
    print('This number must be a multiple of a random number.')
    print('The multiple will change each game. Read the game instructions before playing! \n')
    print('')

    player1Name = input('Enter the name of the first player \n')
    player2Name = input('Enter the name of the second player \n')
    print('')

    for i in range(numOfGames):
        winner = playGame(player1Name, player2Name, i)

        if (winner == player1Name):
            player1Wins = player1Wins + 1
        elif (winner == player2Name):
            player2Wins = player2Wins + 1

    getPlayerStats(player1Wins, player2Wins, player1Name, player2Name)

    return


def playGame(player1Name, player2Name, round):
    multiple = getMultiple()
    correctNum = getCorrectNum(multiple)
    totalTurns = 6
    guessedNumers = []

    instructions(multiple)

    currentPlayer = 0

    for i in range(totalTurns):
        if(len(guessedNumers)):
            print(f'So far the number(s) {guessedNumers} have been guessed')
            print('')

        userGuess = int(input(f'{player2Name if currentPlayer else player1Name}, guess a number \n'))
        print('')

        if(userGuess == correctNum):
            announceVictor(player2Name if currentPlayer else player1Name, correctNum, round)
            return (player2Name if currentPlayer else player1Name)
        else:
            print('Incorrect!')
            isGuessValid(userGuess, multiple, correctNum)
            guessedNumers.append(userGuess)


        currentPlayer = generator(currentPlayer)

    print(f'No one guessed correctly. The secret number was {correctNum}!\n')

    return ''


def instructions(multiple):
    print(f'Each player will have three chances to guess a number between 1 and 100.')
    print(f'For this round, the number must be a mulitple of {multiple}\n')


def getMultiple():
    return random.randint(2,9)


def getCorrectNum(multiple):
    factor = 100/multiple
    divider = random.randint(1, int(factor))

    return (multiple*divider)


def generator(num):
    if (num):
        return 0
    else:
        return 1


def isGuessValid(num, multiple, correctNum):
    if(num%multiple != 0):
        print(f'{num} is not a multiple of {multiple}')
    
    getGuessRange(num, correctNum)


def getGuessRange(num, correctNum): 
    if(num < correctNum):
        print('Your guess is too low \n')
    elif (num > correctNum):
        print('Your guess is too high \n')


def announceVictor(userName,correctNum, round):
    print(f'Congratulations {userName}! The secret number was {correctNum}!')

    if(round <= 1):
        input('Press enter to start the next game...')
    else:
        input('This concludes the final round. \n')


def getPlayerStats(player1Wins, player2Wins, player1Name, player2Name):
    if player1Wins > player2Wins:
        print(f'Congratulations {player1Name} you have won {player1Wins} games in total! You are the best guesser!')
    elif player2Wins > player1Wins:
        print(f'Congratulations {player2Name} you have won {player2Wins} games in total! You are the best guesser!')
    elif (player1Wins == player2Wins and player1Wins > 0):
        print(f'You have both tied with {player1Wins} wins. It looks like you are both great guessers.')
    else:
        return
    

main()