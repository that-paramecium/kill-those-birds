from random import *
from functions.py import *



#define the variables
contBool = True
#set up moves system
moves = ('rock','paper','scissors')
movesCombo = (
    'rock,paper','paper,paper','scissors,paper','paper,rock','rock,rock','scissors,rock'
    'rock,scissors','paper,scissors','scissors,scissors'
    )
ties = [movesCombo[1],movesCombo[4],movesCombo[8]]
userWins = [movesCombo[3],movesCombo[2],movesCombo[7]]
aiWins = [movesCombo[0],movesCombo[6],movesCombo[8]]
#used in main file
def rockPaperScissors():
    while contBool == True:
        userMove = input('what is thine move (rock, paper, scissors')
        if userMove not in moves: 
            raise MoveError
            break
        else:
            aiMove = randchoice(moves)
            resultList = [userMove,aiMove]
            result = ','.join(resultList)
        if result in ties:
            print("It's a tie!")
            exitCheck()
        elif result in userWins:
            print("You won with your {} against my {}".format(userMove,aiMove))
            exitCheck()
        elif result in aiWins:
            print("You lost with my {} against your {}".format(aiMove, userMove))
            exitCheck()
        else:
            raise ResultError
    file1 = open("highscores.txt", "w") 
    file1.write(result)
