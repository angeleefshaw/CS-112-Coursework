import random
import time

def main():
    totalNumberOfCaves = 4 
    treasure = 50
    turns = 0  
    readyToCashOut = 'no'
    
    introduction(treasure)

    while turns < 3 and treasure > 0 and readyToCashOut == 'no':  
        turns = turns + 1 
        cavenumber = choosecave(totalNumberOfCaves)
        readyToCashOut = 'no'
              
        if(cavenumber == 1):
            treasure = friendlyCave(treasure)
        elif (cavenumber == 2):
            treasure = exchangeCave(treasure)
        elif (cavenumber == 3):
            treasure = dangerCave(treasure)
        elif (cavenumber == 4):
            treasure = riddleCave(treasure)
        else:
            print("you're dead!")

        readyToCashOut = (input('Want to cash out? Please type Yes or No \n')).lower()

        if (readyToCashOut == 'no'):
            print('It looks like you want to keep exploring... \n')
     
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

def exchangeCave(treasure):
    print("You have encountered...")
    time.sleep(1)
    print("...the greedy goblin!")
    time.sleep(1)
    if treasure < 25:
        treasure= treasure + random.randint(10, 40)
        print(treasure) 
        print(f"The goblin took some of your coins and made a good investment, now you have {treasure} gold coins!")
    elif treasure >= 25:
        treasure= treasure - random.randint(1, treasure)
        print(treasure) 
        print(f"The goblin took some of your coins and made a terrible investment, now you have {treasure} gold coins!")
    return treasure
     
def dangerCave(treasure):
    print("Adventurer Beware!")
    time.sleep(2)
    print("You were attacked by a horde of murloc!")
    treasure= treasure - random.randint(1, treasure)
    print("They knocked you out and robbed you of your coins...")
    time.sleep(1)
    print(f"...You now have {treasure} gold coin(s) left!")
    return treasure


def riddleCave(treasure):
    riddles = []
    answers = []
    riddles.append("I'm the rare case when today comes before yesterday.")
    answers.append("dictionary")
    riddles.append("I go all the way around the world but stay in a corner.")
    answers.append("stamp")
    riddles.append("I get bigger the more you take away from me.")
    answers.append("hole")



    whichRiddle = random.randint(0, len(riddles) - 1)
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
    cave = random.randint(1, totalNumberOfCaves)
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

    

main()




