from random import shuffle

suiteOfCard = ["Clubs", "Diamonds" ,"Hearts", "Spades"]
nameOfCards = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine" , "Ten", "Jack", "Queen", "King", "Ace"]
cardDict = {}
for i in range(len(nameOfCards)):
    cardDict[nameOfCards[i]] = i+2


class Card():
    def __init__(self, nameCard, suiteCard):
        self.nameCard = nameCard
        self.suiteCard = suiteCard
        self.value = cardDict[nameCard]

    def __str__(self):
        return "{} of {}".format(self.nameCard, self.suiteCard)