from cmath import e
import os

Win = 1
Draw = -1
Running = 0
Game = Running

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")


def CheckPosition(x):
    if(board[x] == ' '):
        return True
    else:
        return False


def CheckWin():
    global Game
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game = Win
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game = Win
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game = Win
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        Game = Win
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        Game = Win
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        Game = Win
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        Game = Win
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        Game = Win
    elif(board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        Game = Draw
    else:
        Game = Running


player = 1
print("Welcome To Tic _ Tac _ Toe")
print("1 | 2 | 3\n--|---|--\n4 | 5 | 6\n--|---|--\n7 | 8 | 9")
name1 = input("Enter Name For Player 1 : ")
name2 = input("Enter Name For Player 2 : ")
print(f"{name1} Has X and {name2} Has O")
while(Game == Running):
    os.system('cls')
    DrawBoard()
    if (player % 2 != 0):
        Mark = 'X'
        name = name1
    else:
        Mark = 'O'
        name = name2

    try:
        Choice = int(input(f"Enter Value {name} : "))
        if(CheckPosition(Choice)):
            board[Choice] = Mark
            os.system('cls')
            DrawBoard()
            player += 1
            CheckWin()
    except:
        pass

os.system('cls')
DrawBoard()
if (Game == Draw):
    print("Game Is Drawn")
else:
    player -= 1
    if (player % 2 != 0):
        print(f"\n\nPLayer One {name1} Has Won.\n\n")
    else:
        print(f"\n\nPLayer Two {name2} Has Won.\n\n")
