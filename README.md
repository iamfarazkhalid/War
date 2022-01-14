# War Game Implementation

## Basic Implementation and Assumptions

- Understood the logic of game from the document provided on Wikipedia.
- The game is played in a simulation setting: Player1 and Player2 enter their name and the game simulation is played rather than player choosing to go in each turn.
- Results for each round are outputted (using print statements) to Command Line Interface.
- User will always enter the correct input for Player names. In CLI, user has to enter names in qoutes i.e ("Player1" instead of Player1).
- In a hypothetical situation where WarGame runs for an improbably long time where we have memory problems (sort of an infinte loop), error handling for that is not implemented.
- Using "shuffle" from random library to shuffle cards, haven't had the chance to look at implementation to make sure shuffling of cards is random to an extent of what shall be required.
    - I did not focus on this too much as if the case was different, it would had been a functional requirement in a real setting.
- Did not take into account any non-functional requirements for the sake of time.
- Did not implement unit/integration tests to thoroughly check the app.
- Number of cards in hand (as displayed in CLI on each round) sum up to 50 and not 52.
    - This is because I've considered two cards always being in play when I display the print statement. So sum of cards in hand will be 50 in a regular play.
    - For each War, cards in hand will decrease by 8 (as each player put 3 cards facing down and one card facing up).
    - Once someone wins a game, cards in hand sum up to after cards for next round are played.

## Future work
- Write unit/integration tests to thoroughly check the application.
- Ideally, I would had implemented a Quality Gate check to make sure code coverage/tests surpass the basic limits set for them.
- Implemented a basic CI/CD pipeline using Github Actions to run tests before merging the code to main branch (to protect the branch).
- Instead of having print statements embedded into the main program, have a seperate file for common prompts and display them accordingly.
- Instead of outputting results in CLI, write to a file for better readibility.
- Check code with Python linter to make sure formatting is according to standard.

## Installation

For this program, I used Python 3.10.

To run the program, please follow the instructons below.

```sh
#Go to the War folder that you downloaded.
cd War
python GameOfWar.py
#When Asked to enter name of players, please enter name in qoutes like below:
Enter First Player Name: "Player1"
Enter Second Player Name: "Player2"
```
