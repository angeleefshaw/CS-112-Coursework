class Player:
    def __init__(self,n,p,r):
        self.name = n
        self.role = r
        self.pointsScored = p


    def __str__(self):
        if self.role == "Captain":
               return(self.name + "\t" + str(self.pointsScored) + "     C")
        else:
            return(self.name + "\t" + str(self.pointsScored) )
#####################################################################


def main():
    players = [
        Player("Eleven",12, "Captain"),
        Player("Lucas",6, "Player"), 
        Player("Mike",3,"Player")      
    ]
    print(players)
    print("Player\tPoints\tRole")
    for thisPlayer in players:
         print(thisPlayer)


    averagePoints =findAveragePointsScored(players)
    print("Scored an average of " + str(averagePoints))


    
def findAveragePointsScored(listp):    
    total = 0
    for thisPlayer in listp:
        total = total + thisPlayer.pointsScored


    average = total/len(listp)
    return(average)


main()
        