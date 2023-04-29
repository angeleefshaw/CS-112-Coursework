from random import randint

class Card:
    def __init__(self, cardValue, suit):
        suitOptions = ['hearts', 'spades', 'diamonds', 'clubs']

        if(suit.lower() in suitOptions):
            self.__suit  = suit
        else:
            print('That suit does not exist.')

        self.__cardValue = cardValue

    def __str__(self):
        rtnStr = f"Your card is the {self.__cardValue} of {self.__suit}"
        return rtnStr
    
card1 = Card('Ace', 'hearts')
card2 = Card('King', 'diamonds')

cardList = [card1, card2]
for card in cardList:
	print(card) 
