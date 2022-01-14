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
    PlayerNumberOne = activePlayer[0]
    PlayerNumberTwo = activePlayer[1]

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
        
        cardsOfPlayerOne = []
        cardsOfPlayerTwo = []
        cardsOfPlayerOne.append(PlayerNumberOne.playCard())
        cardsOfPlayerTwo.append(PlayerNumberTwo.playCard())
        turnIsWar = True

        while (turnIsWar == True):
            #Display each round detail
            print("This is Round Number: {}".format(gameRounds))
            print("{}'s card: {} \n{}'s card: {}".format(firstPlayerName, str(cardsOfPlayerOne[-1]), secondPlayerName, str(cardsOfPlayerTwo[-1])))
            print("Player One Has {} cards!".format(len(PlayerNumberOne.deckOfPlayer)))
            print("Player Two Has {} cards!".format(secondPlayer.lenOfDeck()))

            if (cardsOfPlayerOne[-1].value > cardsOfPlayerTwo[-1].value) :
                PlayerNumberOne.deckOfPlayer.extend(cardsOfPlayerOne)
                PlayerNumberOne.deckOfPlayer.extend(cardsOfPlayerTwo)
                print("{} wins this round!\n".format(firstPlayerName))
                turnIsWar = False
                break
            
            elif (cardsOfPlayerOne[-1].value < cardsOfPlayerTwo[-1].value) :
                PlayerNumberTwo.deckOfPlayer.extend(cardsOfPlayerOne)
                PlayerNumberTwo.deckOfPlayer.extend(cardsOfPlayerTwo)
                print("{} wins this round!\n".format(PlayerNumberTwo.playerName))
                turnIsWar = False
                break
            
            # If condition for War is true, i.e FirstPlayer's card and SecondPlayer's have same rank. We draw 4 cards.
            # Logic above will handle to see the last drawn card out of 4.
            else:
                print("{} and {} have same rank cards! It's time for War!".format(firstPlayerName, secondPlayerName))
                
                #If and else if statement to check if player has enough cards to play the game of War.
                if len(PlayerNumberOne.deckOfPlayer) < 3:
                    print("\n{} does not have enough cards for War.".format(PlayerNumberOne.playerName))
                    print("{} Wins!\n".format(PlayerNumberTwo.playerName))
                    gameActiveStatus = False
                    break

                elif len(PlayerNumberTwo.deckOfPlayer) < 3:
                    print("\n")
                    print("\n{} does not have enough cards for War.".format(PlayerNumberTwo.playerName))
                    print("{} Wins!\n".format(PlayerNumberOne.playerName))
                    gameActiveStatus = False
                    break
                # If players have enough cards to play game of War, draw four cards from their decks.
                else:
                    for i in range(4):
                        cardsOfPlayerOne.append(PlayerNumberOne.playCard())
                        cardsOfPlayerTwo.append(PlayerNumberTwo.playCard())



if __name__ == '__main__':
    main()