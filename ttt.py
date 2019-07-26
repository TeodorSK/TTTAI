from random import randrange

def newBoard():
    #TODO: make better board
    board = [['O', '', 'X'],['X', '', 'X'],['', 'O', 'O']]
    return board

def printBoard(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == '': print('[]', end=" ") #print empty box
            else: print (board[row][col], end=" ") #or actual symbol
            # print (',', end=" ")
        print()

def prompt(player):
    print (player + ", your move.")

def name(player):
    print ("Player " + player + ", whats your name")
    return input()

#passed coords are already valid
#returns the board!!
def moveTo(char, board, coords):
    board[int(coords[0])][int(coords[1])] = char
    return board

def move(player, board):
    #Checking values
    while True:


        if player == 1:
        #USER INPUT
            char = 'X'
            move = minimaxAI(board, char)
            print (move)
            #DEBUG:
            if move == "99" : print( getLegalMoves(board, char))

        #AI INPUT
        if player == 2:
            char = 'O'
            move = input()

        if check_move(board, move):

            break
        else: print("something wrong")


    #check range and place char on board
    board[int(move[0])][int(move[1])] = char

def check_move(board, move):
    try:
        if len(move) == 2:
            move_x = int(move[0])
            move_y = int(move[1])
        else:
            print("enter 2 digits")
            return False
    except ValueError:
        print("Enter a valid int")
        return False
    #range check
    if not move_x in range(3) or not move_y in range(3):
        print("out of range")
        return False
    #check if taken
    if (board[move_x][move_y] != ''):
        print ("that spot is taken try again")
        return False
    else:
        return True

def getWinner(board, p1, p2):
    #check rows and cols
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            print ("winner " + board[row][0])
            winner = p1 if board[0][0] == "X" else p2
            return winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            print ("winner is " + board[0][col])
            winner = p1 if board[0][0] == "X" else p2
            return winner
    #check diag
    if board[0][0] == board[1][1] == board[2][2] != '':
        print ("winner is " + board[0][0])
        winner = p1 if board[0][0] == "X" else p2
        return winner
    if board[0][2] == board [1][1] == board[2][0] != '':
        print ("winner is " + board[0][2])
        winner = p1 if board[0][0] == "X" else p2
        return winner

def is_board_full(board):
    for col in board:
        for sq in col:
            if sq is '':
                return False
    return True

#=====ENGINE=====
def game():
    board = newBoard()
    printBoard(board)
    # p1 = name("1")
    # p2 = name("2")
    p1 = 'X'
    p2 = 'O'

    winner = None
    players = [p1, p2]
    moveCounter = 0

    while True:
        prompt(players[moveCounter%2])
        move(moveCounter%2+1, board) #alternates between player 1 and 2
        printBoard(board)
        winner = getWinner(board, p1, p2)
        if (not winner == None): break
        if is_board_full(board):
            print ("it's a draw")
            winner = "no one"
            break
        moveCounter += 1

    print ("congrats " + winner)

def randAI(board):
    while(True):
        move = str(randrange(3)) + str(randrange(3))
        if check_move(board, move): break
    return move

#example: findHole(board, 'O') Single quotes!!
#finds and returns coordinates of an almost-won row/column/diagonal
#playerSym is "X" or "O"
#currently checks horizontals, verticals, diag1, diag2 and returns only first hole
def findHole(board, playerSym):
    #horizontals
    for row in range(3):
        thisRow = []
        for col in range(3):
            thisRow.append(board[row][col])
        if thisRow.count(playerSym)== 2:
            if '' in thisRow: return (str(row) + str(thisRow.index('')))

    #verticals
    for col in range(3):
        thisCol = []
        for row in range(3):
            thisCol.append(board[row][col])
        if thisCol.count(playerSym)== 2:
            if '' in thisCol: return (str(thisCol.index('')) + str(col))

    #diagonal1
    thisDiag = []
    for dg in range(3):
        thisDiag.append(board[dg][dg])
    if thisDiag.count(playerSym)== 2:
        if '' in thisDiag: return (str(thisDiag.index('')) + str(thisDiag.index('')))

    #diagonal2
    thisDiag = []
    for dg in range(3):
        thisDiag.append(board[dg][2-dg])
    if thisDiag.count(playerSym)== 2:
        if '' in thisDiag: return (str(thisDiag.index('')) + str(2-thisDiag.index('')))

    return "88"

def winningMoveAI(board, char):

    if (char == 'O'): oppChar = 'X'
    else: oppChar = 'O'

    move = findHole(board, char)
    if move == "88" :
        print ("no hole found, random move")
        move = randAI(board)
    else:
        print ("Hole found! I win!")
    return move

def winningBlockingAI(board, char):

    if (char == 'O'): oppChar = 'X'
    else: oppChar = 'O'

    move = findHole(board, char)

    if move == "88" :
        print ("no hole found, trying to block")
        move = findHole(board, oppChar)
    else:
        print ("Hole found! I win!")
        return move

    if move == "88" :
        print ("no blocking moves found either, random move")
        move = randAI(board)
    else:
        print ("block!!")

    return move

#returns score of current state
def minimax_score(board, char):

    if (char == 'O'): oppChar = 'X'
    else: oppChar = 'O'

    if getWinner(board, char, oppChar) == 'X':
        return +10
    elif (getWinner(board, char, oppChar) == 'O'):
        return -10
    elif (is_board_full(board)):
        return 0

    legalMoves = getLegalMoves(board)

    scores = []
    for legalMove in legalMoves:
        newBoard = moveTo(char, board, legalMove)
        score = minimax_score(newBoard, oppChar)
        scores.append(score)



    if char == 'X': return max(scores)
    else: return min(scores)

def minimaxAI(board, char):

    if (char == 'O'): oppChar = 'X'
    else: oppChar = 'O'

    legalMoves = getLegalMoves(board)
    print (legalMoves)
    scores = []
    for legalMove in legalMoves:
        newBoard = moveTo(char, board, legalMove)
        score = minimax_score(newBoard, oppChar)
        scores.append(score)

    #FIX THIS:
    #minimaxAI seems to be called twice?
    #first round returns proper move, then gets called again with no legal moves
    print ("scores for " + char)
    print (scores)


    if char == 'X':
        print("x moves to " + str(legalMoves[scores.index(max(scores))]))
        return str(legalMoves[scores.index(max(scores))])
    else:
        print("o moves to " + str(legalMoves[scores.index(min(scores))]))
        return str(legalMoves[scores.index(min(scores))])

def getLegalMoves(board):

    legalMoves = []

    for row in range(3):
        for col in range(3):
            if board[row][col] == '' :
                legalMoves.append(str(row)+str(col))
                print ("found empty spot at " +str(row)+str(col))

    return legalMoves

retry = "y"
while(retry == "y"):
    game()

    print ("Again? y/n?")
    retry = input()
