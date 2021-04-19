"""
Tic Tac Toe Player
"""

import math
import copy

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
    """
    if board==initial_state() : 
        return X
    if(terminal(board)) :
        return X

    noOfX = board[0].count(X)+board[1].count(X)+board[2].count(X)
    noOfO = board[0].count(O)+board[1].count(O)+board[2].count(O)

    if noOfX > noOfO :
        return O
    else :
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    myset=set()
    #find the empty points in the board 
    for i in range(3):
        for j in range(3):
            if( board[i][j]==EMPTY):
                myset.add((i,j))

    return myset
    

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    #action will have i,j values so 
    if action[0] not in range(0,3) or action[1] not in range(0,3) or board[action[0]][action[1]] is not EMPTY:
        raise Exception("Not Valid")

    boardnew= copy.deepcopy(board)
    boardnew[action[0]][action[1]]= player(board)
    
    return boardnew


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if(board[0][0]==X and board[0][1]==X and board[0][2] ==X)or(board[1][0]==X and board[1][1]==X and board[1][2] ==X)or(board[2][0]==X and board[2][1]==X and board[2][2] ==X)or(board[0][0]==X and board[1][0]==X and board[2][0] ==X)or(board[0][1]==X and board[1][1]==X and board[2][1] ==X)or(board[0][2]==X and board[1][2]==X and board[2][2] ==X)or(board[0][0]==X and board[1][1]==X and board[2][2] ==X)or(board[2][0]==X and board[1][1]==X and board[0][2] ==X):
        return X
    if(board[0][0]==O and board[0][1]==O and board[0][2] ==O)or(board[1][0]==O and board[1][1]==O and board[1][2] ==O)or(board[2][0]==O and board[2][1]==O and board[2][2] ==O)or (board[0][0]==O and board[1][0]==O and board[2][0] ==O)or (board[0][1]==O and board[1][1]==O and board[2][1] ==O)or (board[0][2]==O and board[1][2]==O and board[2][2] ==O)or (board[0][0]==O and board[1][1]==O and board[2][2] ==O)or (board[2][0]==O and board[1][1]==O and board[0][2] ==O):
        return O
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True

    #if no cell on the board is empty
    cnt=0
    for i in range(3) :
        for j in range(3) :
            if board[i][j]==EMPTY :
                 cnt=1
    if cnt==0 :
         return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X :
        return 1
    if winner(board)  == O :
        return -1
    return 0 

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) :
        return None
    
    if player(board) == X :
        bests = -math.inf
        # making all moves to see beforehand what bring the best result 
        for move in actions(board) :
            maxs = min_value(result(board,move)) 
            if maxs > bests :
                bests = maxs
                best_move = move

    elif player(board) == O :
        bests = math.inf 
        for move in actions(board) :
            mins = max_value(result(board,move)) 
            if mins < bests :
                bests = mins
                best_move = move

    return best_move


#defining max_value and min_value functions 
def min_value(board) :
    if terminal(board) :
        return utility(board)

    s = math.inf
    for move in actions(board) :
        s = min(s,max_value(result(board,move)))
    return s

def max_value(board) :
    if terminal(board) :
        return utility(board)

    s = -math.inf
    for move in actions(board) :
        s = max(s,min_value(result(board,move)))
    return s





