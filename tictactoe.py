"""
Tic Tac Toe Player
"""

from cgi import print_form
from copy import deepcopy
from ctypes import util
from hashlib import new
import math
from queue import Empty
import random
from ssl import ALERT_DESCRIPTION_USER_CANCELLED
from tkinter import E

X = "X"
O = "O"
EMPTY = None
class Node():
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.values = {}
        self.action = None
        self.optimal_action = (None, None)
        self.children = {}
        self.place = 0
        self.moves = actions(state)
    def move(self):
        self.place = self.place + 1
    def reset(self):
        self.place = 0
    def eliminate(self):
        self.childs = self.childs[:-1]




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
    """
    o=0
    x=0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                x = x + 1
            if board[i][j] == O:
                o = o + 1
    if o == x:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    Actions = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                Actions.append((i,j))
    return Actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    state=player(board)
    board[action[0]][action[1]] = state
    return board
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for x in range(0,3):

        if board[x][0] == board[x][1] and board[x][0] == board[x][2] and board[x][0] != EMPTY:
            return board[x][0]
        if board[0][x] == board[1][x] and board[0][x] == board[2][x] and board[0][x] != EMPTY:
   
            return board[0][x]
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != EMPTY:
        
        return board[1][1]
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != EMPTY:
        
        return board[1][1]  
    else:
        return None   



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == None:
                empty = empty + 1
    if winner(board) != None or empty == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True and winner(board) == None:
        return 0
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    P = player(board)
    Actions = actions(board)
    Moves = []
    Vals = []
    optimal_move = ()
    if len(Actions) == 9:
        return(random.choice(Actions)) 
    for action in Actions:
        new_board = result(deepcopy(board), action)
        if P == X:
            Moves.append((minval(new_board),action))
        else:
            Moves.append((maxval(new_board),action))
    for move in Moves:
        Vals.append(move[0])
        if P == X:
            if max(Vals) == move[0]:
                optimal_move = move[1]
        else:
            if min(Vals) == move[0]:
                optimal_move = move[1]
    return optimal_move
    

def minval(board): 
    if terminal(board):
        return utility(board)  
    else:
        Vals = []
        Actions = actions(board)
        for action in Actions:
            new_board = result(deepcopy(board), action)
            Vals.append(maxval(new_board))
        
        return min(Vals)

def maxval(board): 
    if terminal(board):
        return utility(board)  
    else:
        Vals = []
        Actions = actions(board)
        for action in Actions:
            new_board = result(deepcopy(board), action)
            Vals.append(minval(new_board))
        return max(Vals)

board =    [[EMPTY, O, EMPTY],
            [X, X, O],
            [O, X, EMPTY]]
print(minimax(board))




