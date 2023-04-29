from random import randint

class Player:
    def __init__(self):
        self.__score  = 0

    def playRound(self):
        randomVal = randint(1, 2)

        if(randomVal == 1):
            self.setScore(2)
        else:
            if(self.__score > 0):
                self.setScore(-1)

    def setScore(self, score):
        self.__score = self.__score + score

    def getScore(self):
        return self.__score

    def __str__(self):
        if(self.__score == 0):
            rtnStr = f"Your score is {self.__score}. Play a round!"
        else: 
            rtnStr = f"Your score is {self.__score}."
        return rtnStr
        
player1 = Player()
player1.playRound()
player1.playRound()
player1.playRound()
print(player1)