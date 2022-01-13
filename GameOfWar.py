from CreateCards import Card
from DeckOfCards import Deck
from GamePlayer import ParticipatingPlayer
from random import shuffle

def main():
    activePlayer = []
    cardsDeck = Deck()
    gameRounds = 0

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

    gameActiveStatus = True
    PlayerNumberOne = current_players[0]
    PlayerNumberTwo = current_players[1]

    while gameActiveStatus:
        gameRounds += 1

        if len(PlayerNumberOne.deckOfPlayer) == 0:
            print("{} : You have an empty deck now.\n".format(PlayerNumberOne.playerName))
            print( "{} is the winner.\n".format(PlayerNumberTwo.playerName))
            gameActiveStatus = False
            break

        elif len(PlayerNumberTwo.deckOfPlayer) == 0:
            print("{} : You have an empty deck now.\n".format(PlayerNumberTwo.playerName))
            print("{} is the winner.\n".format(PlayerNumberOne.playerName))
            gameActiveStatus = False
            break
        
        else:
            #Implement War Game Logic

if __name__ == '__main__':
    main()