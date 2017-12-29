from functions import *
import time
import sys
import os

strategyFile = "strategy.csv"

if not os.path.exists(strategyFile):
    headDf = pd.DataFrame(columns=["Previous", "Next"])
    headDf.to_csv(strategyFile, index=False)

state = [1, 1, 1, 1]
updatePicture(state)
drawState(first=True)
turn = 0
shift = random.randint(0, 1)  # who goes first?
player = input("Would you like to play against me?\n\
Yes-play against computer, No-play against human(y/n)\t")
if "n" in player.lower():
    player = "human"
else:
    player = "computer"

mic = True
micAns = input("Would you like to use the microphone for your speech input?(y/n)")
if len(micAns) > 0:
    if micAns[0].lower() == 'n':
        mic = False

# game loop
while gameOver(state) == -1:
    if (turn + shift) % 2 == 0:  # computer move
        if player == "computer":
            print("My turn")
            time.sleep(0.5)
            state = advanceState(state)
            time.sleep(1)
        else:
            print("Player turn")
            state = inputState(state)
    else:
        print("Player turn")
        promptMove()
        # note the state assumes the current player is listed first
        state = invertState(state)
        # make the choice
        state = inputState(state, mic=mic)
        # we must flip twice
        state = invertState(state)
    turn += 1
    updatePicture(state)
    drawState()
    sayState(state)

print("Nice game")