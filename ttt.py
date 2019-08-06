from random import randrange
import copy

def newBoard():
    #TODO: make better board
    board = [['', '', ''],['', '', ''],['', '', '']]
    return board

def printBoard(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == '': print('[ ]', end=" ") #print empty box
            else: print ("[" + board[row][col] + "]", end=" ") #or actual symbol
        print()

def prompt(player):
    print (player + ", your move.")

def name(player):
    print ("Player " + player + ", whats your name")
    return input()

#passed coords are already valid
#returns the board!!
def moveTo(char, board, coords):
    _board = copy.deepcopy(board)
    _board[int(coords[0])][int(coords[1])] = char
    return _board


#TODO: let game.py modify these vars
P1 = "winningAI"
P2 = "minimaxAI"

def setP1AI(_P1):
    P1 = str(_P1)

def setP2AI(_P2):
    P2 = str(_P2)

def move(player, board):

    if player == 1:
        char = 'X'
        AI = P1
    elif player == 2:
        char = 'O'
        AI = P2

    print ("poop" + AI)

    while True:
        if AI == "winningAI": move = winningMoveAI(board, char)
        elif AI == "minimaxAI": move = minimaxAI(board, char)
        elif AI == "blockingAI": move = winningBlockingAI(board, char)
        elif AI == "randomAI": move = randAI(board, char)

        if check_move(board, move): break

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
    if (not board[move_x][move_y] == ''):
        print ("that spot is taken try again")
        return False
    else:
        return True

def getWinner(board):
    all_line_co_ords = get_all_line_co_ords()

    for line in all_line_co_ords:
        line_values = [board[x][y] for (x, y) in line]
        if len(set(line_values)) == 1 and line_values[0] is not None:
            return line_values[0]

    return None


def get_all_line_co_ords():
    cols = []
    for x in range(3):
        col = []
        for y in range(3):
            col.append((x, y))
        cols.append(col)

    rows = []
    for y in range(3):
        row = []
        for x in range(3):
            row.append((x, y))
        rows.append(row)

    diagonals = [
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    return cols + rows + diagonals

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
    p1 = 'X'
    p2 = 'O'

    winner = None
    players = [p1, p2]
    moveCounter = 0

    while True:
        prompt(players[moveCounter%2])
        move(moveCounter%2+1, board) #alternates between player 1 and 2
        printBoard(board)
        winner = getWinner(board)
        if (winner == 'X' or winner == 'O'): break
        if is_board_full(board):
            print ("it's a draw")
            winner = "no one"
            break
        moveCounter += 1

    print ("congrats " + winner)

    return winner

def randAI(board, char):
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
        move = randAI(board, char)
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
        move = randAI(board, char)
    else:
        print ("block!!")

    return move

def minimax_score_cache(board, char):
    if char == 'X': cache=cache_X
    elif char == 'O': cache=cache_O

    board_id = str(board)
    if board_id not in cache:
        if (char == 'O'): oppChar = 'X'
        else: oppChar = 'O'

        winner = getWinner(board)
        if (winner == 'X'):
            return 10
        elif (winner == 'O'):
            return -10
        elif (is_board_full(board)):
            return 0

        legalMoves = getLegalMoves(board)

        scores = []
        for legalMove in legalMoves:
            if check_move(board, legalMove):
                _board = copy.deepcopy(board)
                newBoard = moveTo(char, _board, legalMove)
                score = minimax_score_cache(newBoard, oppChar)
                scores.append(score)


        if char == 'X': cache[board_id] = max(scores)
        else: cache[board_id] = min(scores)
    return cache[board_id]

#returns score of current state
cache_X={}
cache_O={}
def minimax_score(board, char):

    if (char == 'O'): oppChar = 'X'
    else: oppChar = 'O'

    winner = getWinner(board)
    if (winner == 'X'):
        return 10
    elif (winner == 'O'):
        return -10
    elif (is_board_full(board)):
        return 0

    legalMoves = getLegalMoves(board)

    scores = []
    for legalMove in legalMoves:
        if check_move(board, legalMove):
            _board = copy.deepcopy(board)
            newBoard = moveTo(char, _board, legalMove)
            score = minimax_score(newBoard, oppChar)
            scores.append(score)

    if char == 'X': return max(scores)
    else: return min(scores)

def minimaxAI(board, char):

    if (char == 'O'): oppChar = 'X'
    else: oppChar = 'O'

    legalMoves = getLegalMoves(board)
    scores = []
    for legalMove in legalMoves:
        if check_move(board, legalMove):
            _board = copy.deepcopy(board)
            newBoard = moveTo(char, _board, legalMove)
            score = minimax_score_cache(newBoard, oppChar)
            scores.append(score)

    if char == 'X':
        return str(legalMoves[scores.index(max(scores))])
    else:
        return str(legalMoves[scores.index(min(scores))])

def getLegalMoves(board):

    legalMoves = []

    for row in range(3):
        for col in range(3):
            if board[row][col] == '' :
                legalMoves.append(str(row)+str(col))

    return legalMoves

def driver(rounds):
    X_wins = 0
    O_wins = 0
    draws = 0
    for i in range(int(rounds)):

        winner = game()
        if winner == 'X': X_wins += 1
        elif winner == 'O': O_wins += 1
        elif winner == 'no one': draws += 1

    return (str(X_wins) + " " + str(O_wins) + " " + str(draws))
