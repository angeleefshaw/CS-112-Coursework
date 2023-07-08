from random import randint

class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        rtnStr = f"Your card is the {self.name} of {self.value}"
        return rtnStr

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        status = 'active'

    def __str__(self):
        rtnStr = f"Hello {self.name}, you are holding {self.hand} in your hand"
        return rtnStr
    
    def get_hand_value(self):
        value = 0

        for i in range(len(self.hand)):
            value = value + self.hand[i].value

        return value
     
    def set_hand_value(self, cards):
        for card in cards:
            self.hand.append(card)
        return
    
    def set_status (self, status):
        self.status = status
        return

    def get_hand_total(self):
        value = 0

        for i in range(len(self.hand)):
            value = value + self.hand[i].value

        for i in range(len(self.hand)):
            if(self.hand[i].name == 'ace'):
                if(value == 11):
                    value = 21
                    
        return value


def main ():
    players = []
    hasWinner = False
    rounds = 2

    #call instructions
    instructions()

    #create/define players using Player class(2 max)
    player_1 = input('What is the name of the first player? ')
    player1 = Player(player_1)

    player_2 = input('What is the name of the second player? ')
    player2 = Player(player_2)

    dealer = Player('Dealer')

    players.append(player1)
    players.append(player2)
    players.append(dealer)

    deck = create_deck()

    # Deal two cards to each player
    for player in players:
        player.set_hand_value(deal(deck, 2))

    #Check hand of each player (player1....dealer) for blackjack
    for player in players:
        playerHand = player.get_hand_total()

        if(int(playerHand) == 21):
            print(f'{player.name} has Blackjack! {player.name} wins this round.')
            hasWinner = True
            exit

        if(int(playerHand) > 21):
            print(f"{player.name} has busted! {player.name} is out of the game.")
            players.remove(player)

    #Hit or stay?
    while hasWinner == False and rounds > 0:
        hit_or_stay(players, deck, hasWinner)
        rounds = rounds - 1

    if(len(players) == 1):
        print(f'{player.name} has won!')
        hasWinner = True
    else:
        print('Its a tie!')


    return


def instructions():
    print('Welcome to Blackjack! ....')

#INPUT none
#RETURNS list of 52 card objects
def create_deck():
    # Set up local variables
    suits = ['Spades','Hearts','Clubs','Diamonds']
    special_values = {'ace':1, 'king':10, 'queen':10, 'jack':10}

    # Create list of all the card values
    numbers = ['ace', 'king', 'queen', 'jack']
    for i in range(2,11):
        numbers.append(str(i))

    # Initialize deck
    deck = []
    for suit in suits:
        for num in numbers:
            # Values 2-10.
            if num.isnumeric(): 
                card = Card(num, int(num))
            # Ace, King, Queen, or Jack.
            else: 
                card = Card(num,  special_values[num])

            deck.append(card)
    return deck

#INPUT deck and card cound
#RETURNS list of card objects
def deal(deck, count):
    cards = []

    for i in range(count):
        rand_index = randint(1, len(deck))
        removed_el = deck.pop(rand_index)
        cards.append(removed_el)

    return cards

def hit_or_stay (players, deck, hasWinner):
    for player in players:
        if(player.name == 'Dealer'):
            dealer_hit_or_stay(player, deck, hasWinner)
        else :
            h_or_s = input(f'{player.name} your hand value is {player.get_hand_value()}. Do you want to hit or hold (type hit or stay)? ')

            if(h_or_s == 'hit'):
                player.set_hand_value(deal(deck, 1))
                if(check_hand(player, hasWinner) == False):
                    players.remove(player)
    return

def dealer_hit_or_stay (dealer, deck, hasWinner):
    if(dealer.get_hand_total() <= 16):
        print('Dealer must hit!')
        dealer.set_hand_value(deal(deck, 1))
        check_hand(dealer, hasWinner)

def check_hand (player, hasWinner): 
    #Check hand of each player (player1....dealer) for blackjack
    playerHand = player.get_hand_total()

    if(int(playerHand) == 21):
        print(f'{player.name} has Blackjack! {player.name} wins!')
        hasWinner = True
        return True

    if(int(playerHand) > 21):
        print(f"{player.name} has busted! {player.name} is out of the game.")
        return False


main()