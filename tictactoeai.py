import random
def display_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
def inputPlayerLetter():
    mark = ''
    while not (mark == 'X' or mark == 'O'):
        print('Do you want to be X or O?')
        mark = input().upper()
    if mark == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
def firstChance():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
def playAgain():
    print('Do you want to play again? (yes or no)')
    ch=input()
    l=['yes','Yes','YES','y','Y']
    if(ch in l):
        return True
    else:
        return False
def makeMove(board, mark, move):
    board[move] = mark
def isWinner(board, le):
    return ((board[7] == le and board[8] == le and board[9] == le) or 
    (board[4] == le and board[5] == le and board[6] == le) or 
    (board[1] == le and board[2] == le and board[3] == le) or 
    (board[7] == le and board[4] == le and board[1] == le) or 
    (board[8] == le and board[5] == le and board[2] == le) or 
    (board[9] == le and board[6] == le and board[3] == le) or 
    (board[7] == le and board[5] == le and board[3] == le) or 
    (board[9] == le and board[5] == le and board[1] == le)) 
def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard
def isSpaceFree(board, move):
    return board[move] == ' '
def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    if isSpaceFree(board, 5):
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True
print('Welcome to Tic Tac Toe!')
while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = firstChance()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            display_board(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                display_board(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                display_board(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    if not playAgain():
        break