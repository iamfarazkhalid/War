from random import shuffle

class ParticipatingPlayer():
    def __init__(self, name):
        self.playerName = name
        self.deckOfPlayer = []

    def __str__(self):
        return "{} has {} cards at the moment".format(self.playerName, len(self.deckOfPlayer))

    def addCardToDeck(self, card):
        self.deckOfPlayer.append(card)
        shuffle(self.deckOfPlayer)

    def playCard(self):
        shuffle(self.deckOfPlayer)
        return self.deckOfPlayer.pop()

    def viewCards(self):
        for card in self.deckOfPlayer:
            print(card)

    def lenOfDeck(self):
        print("Card in Hand: {}".format(len(self.deckOfPlayer)))