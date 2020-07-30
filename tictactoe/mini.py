import sys
import math
import copy


X = 'X'
O = 'O'
EMPTY = None

player_turn = 1

board= [[O, X, X],
    [X, O, O],
    [X, O, X]]

def player(board):
    counter = 0
    for i in board:
        for j in i:
            if j is None:
                counter += 1
    print (counter)
    #si el numero no te residu (es parell), i no es igual a 0 (que significa que no hi han moviments):
    if (counter % 2 ==0 and counter != 0):
        return O
    #si es 0 vol dir que no hi han moviments, n oes el torn de ningu i retorno None
    elif (counter == 0):
        return EMPTY

    else:
        return X


    print (counter)
    print (player_turn)


def actions(board):

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

    return (possible_actions)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    
    If the X player has on the game, function should return x. Same for O

    One can win if three of their moves ina row horizontally, vertically, diagonally.

    Assume that there will be AT MOST one winner

    If there is no winner function should return None
    """
    win_player = EMPTY
    #un altre metode per comprovar tres en rlla horitzontal, pero agafo l'altre aixi horitzontla i vertical son el mateix
    # for i in board:
    #     check = i[0]
    #     for j in i:
    #         if j == check:
    #             print ("Same as before, keep going")
    #             print j
    #         else return None
    #comprovo si hi ha 3 en ralla HORITZONTAL
    for i in range(0,2):
        if board[i][0] == board[i][1]:
            if board[i][0] == board[i][2]:
                win_player = board[i][0]
                print(f"tres en ralla horitzonal de {win_player}")
                return win_player       
        else:
            win_player = EMPTY


    #comprovo si hi ha 3 en ralla VERTICAUl (ve a ser el mateix que horitzonal tot ique primer miro les j)
    for i in range(0,2):
        if board[0][i] == board[1][i]:
            if board[0][i] == board[2][i]:
                win_player = board[0][i]
                print(f"tres en ralla vertical de {win_player}")
                
                return win_player
        else:
            win_player = EMPTY


    #comprovo si hi ha 3 en ralla DIAGONAL
    if board[0][0] == board[1][1] and  board[0][0] == board[2][2]:
        win_player = board[0][0]
        print (f"Tres en ralla diagonal <- de {win_player}")
        return win_player
    elif board[0][2] == board[1][1] and  board[0][2] == board[2][0]:
        win_player = board[0][2]
        print (f"Tres en ralla diagonal -> de {win_player}")
        return win_player
    else:
        win_player = EMPTY

    if win_player == None:
        print ("Nobody wins")
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    It will return True if there aren't moves to do in the board or if someone has win
    """
    #If there are no moves:
    if player(board) == None or winner(board) == X or winner(board) == O:
        print("no moves or win")
        return True
    else:
        return False

terminal(board)
