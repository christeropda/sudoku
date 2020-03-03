import numpy as np
import time
from random import randint

def solve(board):
    # time.sleep(1)
    # print(board)
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                for i in range(1,10):
                    if(test_fit(x, y, i, board)):
                        board[x][y] = i
                        if(solve(board)):
                            return True
                        board[x][y] = 0
                return False
            else:
                if(check_board(board)):
                    return True
    
    return 

def check_board(board):
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                return False
    return True

def test_fit(x, y, number, board):
    for i in range(9):
        if board[x][i] == number:
            return False
    
    for j in range(9):
        if board[j][y] == number:
            return False
    
    xcord = (x // 3) * 3
    ycord = (y // 3) * 3

    for k in range(3):
        for l in range(3):
            if board[xcord+k][ycord+l] == number:
                return False

    return True

grid = np.array([
    [8, 6, 5, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 2, 1],
    [0, 0, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 1, 3, 0],
    [4, 0, 0, 1, 0, 0, 0, 0, 0],
    [9, 0, 0, 0, 0, 6, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 5, 0],
    [5, 0, 0, 4, 0, 0, 2, 6, 0],
    [0, 0, 3, 0, 6, 0, 0, 0, 0]
    ])

solve(grid)
print(grid)