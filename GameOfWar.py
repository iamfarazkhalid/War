from CreateCards import Card
from DeckOfCards import Deck
from GamePlayer import ParticipatingPlayer
from random import shuffle

def main():
    activePlayer = []
    cardsDeck = Deck()

    firstPlayerName = str(input("Enter First Player Name: "))
    firstPlayer = ParticipatingPlayer(firstPlayerName)

    secondPlayerName = str(input("Enter Second Player Name: "))
    secondPlayer = ParticipatingPlayer(secondPlayerName)

    activePlayer.append(firstPlayer)
    activePlayer.append(secondPlayer)

    #Give 26 cards to each player
    for i in range(26):
        firstPlayer.addCardToDeck(cardsDeck.popCard())
        secondPlayer.addCardToDeck(cardsDeck.popCard())

if __name__ == '__main__':
    main()