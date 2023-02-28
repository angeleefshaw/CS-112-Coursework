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
     
def dangerCave(treasure):
    print("Adventurer Beware!")
    time.sleep(2)
    print("You were attacked by a horde of murloc!")
    treasure= treasure - random.randint(1, treasure)
    print("They knocked you out and robbed you of your coins...")
    time.sleep(1)
    print(f"...You now have {treasure} gold coin(s) left!")
