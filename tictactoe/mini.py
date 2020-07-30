import sys
import math
import copy


X = 'X'
O = 'O'
EMPTY = None

player_turn = 1

board= [[X, X, O],
    [O, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]]

def player(board):
	counter = 0
	for i in board:
		for j in i:
			if j is None:
				counter += 1

	if (counter % 2 ==0):
		return O
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


action=(1,1)

if action in actions(board):
    new_board = copy.deepcopy(board)
    print (new_board)
    new_board[action[0]][action[1]]=player(board)
    print (new_board)

else:
    raise Exception("This action cannot be implemented in this board")