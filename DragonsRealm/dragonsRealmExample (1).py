import random
import time

def main():
    introduction()
    totalNumberOfCaves = 1   # right now there's just one cave
    # give the player some starting treasure
    treasure = 50
    turns = 0  
    while turns < 3:  # you will change this so that the player can stop early
                      #or the game can stop them if they have 0 or negative treasure
        turns = turns + 1 
        cavenumber = choosecave(totalNumberOfCaves)
        print(cavenumber) # good for debugging. Perhaps improve or remove later
        
        if(cavenumber == 1):
            treasure = friendlyCave(treasure)
        elif (cavenumber > 1):  # Persons 3-6 will write additional elif caves
            print("These caves haven't been dug yet")
        else:
            print("you're dead!")

    report(treasure)
    
def friendlyCave(treasure):
    #cave number 1: friendly
    #customize before turning in
    print ("You have encountered...")
    time.sleep(3)
    print("...the friendly dragon!")
    print("She has given you treasure!")
    treasure= treasure + random.randint(1,11)
    #customize before turning in 
    print ("and you now have " + str(treasure)+ " gold coins!")
    return(treasure)


def introduction(treasure):
    msg = "Welcome to Dragon's Realm!"
    msg += "\n\n\t" + "*" * 10
    msg += "\n\tYou are a weary traveler navigating"
    msg += "\n\tmany caves. You begin your voyage with "
    msg += "\n\t" + str(treasure) + " gold coins."
    msg += "\n\tYour adventure ends when you decide"
    msg += "\n\tyou cannot go any further or you lose"
    msg += "\n\tall of your gold."
    msg += "\n\t" + "*" * 10
    msg += "\n\nGood luck on your adventure!"
    print(msg)
    
def choosecave(totalNumberOfCaves):
        print("Here's where you will set up a system to choose the next cave number")
        print("ask client? perhaps with a random number generator? to pick a cave number")
        cave = totalNumberOfCaves  # right now the cave is always cave 1 bc there's just one cave
        return cave

def report(treasureLeft):
    msg = "\nYour adventure ends!"
    if treasureLeft > 50:
        msg += "\nYou leave this world wealthy."
    elif treasureLeft > 15:
        msg += "\nYou leave with enough for a meal and a night's rest."
    elif treasureLeft > 0:
        msg += "\nYou leave and must now forage for food."
    else:
        msg += "\nYou have lost everything."
    msg += "\nUntil we meet again in Dragon's Realm!"
    print(msg)

def riddleCave(treasure):
    riddles = []
    answers = []
    riddles.append("I'm the rare case when today comes before yesterday.")
    answers.append("dictionary")
    riddles.append("I go all the way around the world but stay in a corner.")
    answers.append("stamp")
    riddles.append("I get bigger the more you take away from me.")
    answers.append("hole")

    print(len(riddles)-1)
    


    whichRiddle = random.randint(0, len(riddles) - 1)
    print(whichRiddle)
    print(riddles[whichRiddle])
    guess = input("What am I? a ____:")
    answer = answers[whichRiddle]
    if guess.lower() == answer:
        print("You are wise!  I will give you 10 coins!")
        treasure += 10
    else:
        print(f"Foolish! The answer was {answer}.")
        print("I will take away 5 coins")
        treasure -= 5
    return treasure
    






