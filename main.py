import random

def suits():
    return ["\u2663", "\u2665", "\u2666", "\u2660"]
def ranks():
    return ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

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

    def addCard(self, card):
        self.hand.append(card)

    def drawCard(self):
        card = card_deck.getCard()
        self.hand.append(card)
        card_deck.removeCard(card)

    def cardCheck(self, card):
        if card in self.hand:
            return True
        else:
            return False


    def rankCheck(self, cardRank, other):
        


    def __str__(self):
        return ', '.join([str(card) for card in self.hand])

    def __repr__(self):
        return self.__str__()


def checkPairs(player_hand, player_pile):
    hand = player_hand.getHand()
    ii = 0
    while ii < len(hand) - 1:
        jj = ii + 1
        while jj < len(hand):
            if hand[ii].compareRanks(hand[jj]):
                player_pile.append(hand[ii])
                player_pile.append(hand[jj])
                player_hand.removeCard(hand[jj])
                player_hand.removeCard(hand[ii])
                i = 0
                break
            else:
                jj += 1
        else:
            ii += 1


def cardExchange(player_hand, other_player_hand, card):
    receiving_hand = player_hand.getHand()
    giving_hand = other_player_hand.getHand()
    giving_hand.removeCard(card)
    receiving_hand.addCard(card)


def botRequest(player_hand, other_player_hand):
    receiving_hand = player_hand.getHand()
    giving_hand = other_player_hand.getHand()
    card = random.choice(receiving_hand)
    cardRank = card.getRank()
    answer = input("Do you have a " + str(cardRank) + "");
    hasCard = giving_hand.RankCheck(cardRank, receiving_hand) #This is currently not working
    if (answer.upper() == "yes".upper()) and hasCard:
        cardExchange(receiving_hand, giving_hand, card)
    else:
        print("  _\n><_>") # todo make a better fish
        bot_hand.drawCard()


def endTurn(turn):
    if turn == 1:
        turn = 0
    else:
        turn = 1

def botTurn():
    checkPairs(bot_hand, bot_pile)
    botRequest(bot_hand, user_hand)
    checkPairs(bot_hand, bot_pile)
    endTurn(current_turn)


# Startup Tasks
card_deck = Deck()
user_hand = Hand(7)
bot_hand = Hand(7)
user_pile = []
bot_pile = []
card_deck.shuffleCards()
current_turn = 0 #random.choice([0, 1])

print(user_hand)
print(bot_hand)
botTurn()
print(bot_hand)

# Hearts: \u2665
# Diamonds: \u2666
# Clubs: \u2663
# Spades: \u2660

