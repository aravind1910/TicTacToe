import random

game=[[0,0,0],[0,0,0],[0,0,0]]

def display_board():
    for i in range(3):
        for j in range(3):
            print(game[i][j],end=' ')
        print()

def row_win(player):
    for i in range(3):
        if(game[i][0]==player and game[i][1]==player and game[i][2]==player):
            return True
        else:
            return False

def col_win(player):
    for i in range(3):
        if(game[0][i]==player and game[1][i]==player and game[2][i]==player):
            return True
        else:
            return False

def diag_win(player):
    if(game[0][0]==player and game[1][1]==player and game[2][2]==player) or (game[2][0]==player and game[1][1]==player and game[0][2]==player):
        return True
    else:
        return False

def winning(i):
    if(row_win(i) or col_win(i) or diag_win(i)):
        return True
        
    if(0 not in game[0] and 0 not in game[1] and 0 not in board[2]):
        return -1

def empty():
    l=[]
    for i in range(3):
        for j in range(3):
            if(game[i][j]==0):
                l.append([i,j])
    return l

def computer_choice():
    empty_spaces=empty()
    loc=random.choice(empty_spaces)
    game[loc[0]][loc[1]]='O'

def play():
    display_board();
    winner=None
    name=input("Please Enter Your Name: ")
    while(winner==None):
        for player in ['X','O']:
            while(1):
                print("Enter the position you want to put your mark: ")
                i,j=input().split()
                i,j=int(i),int(j)
                if(game[i][j]!=0):
                    print("Invalid Position.")
                else:
                    game[i][j]='X'
                    break
            if(winning('X')==True):
                print("Congratulations ",name,"! You Won")
                winner=1
                break
            if(winning('X')==-1):
                print("The Game is a draw!")
                winner=1                
                break
            computer_choice()
            if(winning('O')==True):
                print("Better Luck Next time ",name,", The Computer wins.")
                winner=1
                break
            if(winning('X')==-1):
                print("The Game is a draw!")
                winner=1
                break
            display_board()

play()



