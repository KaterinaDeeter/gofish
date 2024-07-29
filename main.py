import random

def suits():
    return ["\u2663", "\u2665", "\u2666", "\u2660"]
def ranks():
    return ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Card:

    def __init__(self, card_rank, card_suit):
        self.rank = card_rank
        self.suit = card_suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def compareRanks(self, other):
        return self.rank == other.rank

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __str__(self):
        return self.rank + " of " + self.suit

    def __repr__(self):
        return self.__str__()

class Deck:
    def __init__(self):
        self.contents = [Card(rank, suit) for rank in ranks() for suit in suits()]

    def getContents(self):
        return self.contents

    def getCard(self):
        card = random.choice(self.contents)
        return card

    def isEmpty(self):
        deck_empty = False
        if not self.contents:
            deck_empty = True
        return deck_empty

    def removeCard(self, card):
        if card in self.contents:
            self.contents.remove(card)

    def shuffleCards(self):
        return random.shuffle(self.contents)

class Hand:
    def __init__(self, hand_size):
        self.hand = []
        for ii in range(hand_size):
            self.drawCard()

    def getHand(self):
        return self.hand

    def isEmpty(self):
        hand_empty = False
        if not self.hand:
            hand_empty = True
        return hand_empty

    def removeCard(self, card):
        if card in self.hand:
            self.hand.remove(card)

    def drawCard(self):
        card = card_deck.getCard()
        self.hand.append(card)
        card_deck.removeCard(card)


# Startup Tasks
card_deck = Deck()
user_hand = Hand()
bot_hand = Hand()
card_deck.shuffleCards()

# What comes next?
# 1. Decks and Hands can now be created. This means that the game is ready to be started
# 2. With this, I need to create the appropriate behaviors. I have objects but what am I going to be doing with them?
    # Bot Turn
        #check empty, request card, receive card, check for pairs (twice in a turn), potentially draw, end turn
    # User Turn
        #check empty, check pairs, request, receive, check, draw, end turn

# Hearts: \u2665
# Diamonds: \u2666
# Clubs: \u2663
# Spades: \u2660

