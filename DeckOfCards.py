from random import shuffle
from CreateCards import Card

suiteOfCard = ["Clubs", "Diamonds" ,"Hearts", "Spades"]
nameOfCards = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine" , "Ten", "Jack", "Queen", "King", "Ace"]
cardDict = {}

for i in range(len(nameOfCards)):
    cardDict[nameOfCards[i]] = i+2

class Deck():
    def __init__(self):
        self.playerDeck = []

        for nameOfCard in nameOfCards:
            for suiteOfCards in suiteOfCard:
                temp_card = Card(nameOfCard,suiteOfCards)
                self.playerDeck.append(temp_card)

        shuffle(self.playerDeck)

    def popCard(self):
        return self.playerDeck.pop()

    def shuffleDeck(self):
        shuffle(self.playerDeck)

    def __str__(self):
        return "Deck has {} cards".format(len(self.playerDeck))