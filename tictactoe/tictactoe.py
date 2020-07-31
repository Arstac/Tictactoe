"""
Tic Tac Toe Player
"""

import math
import copy
from util import Node, StackFrontier, QueueFrontier

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    We can do it by different ways.
        - Considering that X player will always start, and we have a counter for each move (starting at 0), 
            X player will always move when the counter is even, thus O player will move when the counter is odd
        - Other way to do it is counting the number of moves that have been done.
        - Other way to do it is counting the number of emptys slots. 

            9,7,5,3,1 EMPTYS -> X Turn
            8,6,4,2 EMPTYS -> O Turn
            0 EMPTYS -> Game is over

    """
    counter = 0

    for i in board:
        for j in i:
            if j is None:
                counter += 1
    #si el numero no te residu (es parell), i no es igual a 0 (que significa que no hi han moviments):
    if (counter%2 == 0 and counter != 0):
        return O
    #si es 0 vol dir que no hi han moviments, n oes el torn de ningu i retorno None
    elif (counter == 0):
        return None
    #si no es cap cas anterior, nomes pot ser el torn de X
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    row = 0
    col = 0
    possible_actions = []
    for i in board:
        col=0
        for j in i:
            if j is None:
                possible_actions.append((row,col))
            col+=1
        row+=1
    row=0
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.

    1. Here i get a board, and an action. I have to check that if this action can be done in this state(board).

    2. If action is not valid action for the board, raise and exception

    3. If action is valid -> return a new board state with the original board state plus the move at the cell indicated by the input action

    4. Original board sould be left unmodified

    """

    #First lets check if this action can be done in this board.

    if action in actions(board):
        #We create a deep copy of our board
        new_board = copy.deepcopy(board)

        #We replace the value of the new_board by X or O, depending of the turn
        new_board[action[0]][action[1]]=player(new_board)
        #
        return new_board

        #o be seleccionant action[0] i action[1], on  el primer fa referencia a la fila, i el segon a la columna

    else:
        raise Exception("This action cannot be implemented in this board")

    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    
    If the X player has on the game, function should return x. Same for O

    One can win if three of their moves ina row horizontally, vertically, diagonally.

    Assume that there will be AT MOST one winner

    If there is no winner function should return None
    """

    win_player = EMPTY


    if three_in_row(board) != None:
        return three_in_row(board)

    elif three_in_col(board) != None:
        return three_in_col(board)

    elif three_in_diag(board) != None:
        return three_in_diag(board)

    else:
        return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    It will return True if there aren't moves to do in the board or if someone has win
    """
    #If there are no moves:
    if player(board) == None or winner(board) == X or winner(board) == O:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.

    utility will only be called on a board if terminal(board) is true.
    """
    #comprovo si el joc ha acabat
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
#only call utility if terminal(board) is true

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    print("minmax")
    if terminal(board):
        return None
    #en cas que comenci la maquina, que coloqui la X al mig.
    elif board == initial_state() and player(board) == X:
        print("tir x inicial")
        return (1,1)
    else:
        points = []
        possible_moves = actions(board)
        if player(board) == X:
            print("player X")
            for action in actions(board):
                print("action")
                print (action)
                print ("value:")
                print(min_value(result(board,action)))
                points.append(min_value(result(board,action)))
            print (possible_moves[points.index(max(points))])
            return possible_moves[points.index(max(points))]

        if player(board) == O:
            print ("player O")
            for action in actions(board):
                points.append(max_value(result(board,action)))
            return possible_moves[points.index(min(points))]
        #given a state (s) in this case, board:
        #MAX picks and action a in actions(s) that produces MAX value of min_value(result(s,a))
        #MIN picks and action a in actions(s) that produces MIN value of max_value(result(s,a))

    
def max_value(board):
    if terminal(board):
        return utility(board)
    v=-999999999
    for action in actions(board):
        v=max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v=999999999
    for action in actions(board):
        v=min(v, max_value(result(board, action)))
    return v

def three_in_row(board):
    for row in board:
        if row[0] == row[1] and row[0] == row[2]:
            return row[0]
    return None


def three_in_col(board):
    for i in range(3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return board[0][i]
    return None



def three_in_diag(board):
    if board[0][0] == board[1][1] and  board[0][0] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and  board[0][2] == board[2][0]:
        return board[0][2]
    else:
        return None