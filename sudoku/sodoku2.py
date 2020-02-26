import numpy as np
import time
from random import randint
import sys

#0,0    0,3     0,6
#1,0
#2,0
#3,0    3,3     3,6
#4,0
#5,0
#6,0    6,3     6,6
#7,0
#8,0
#9,0       

def solve_board(board):  
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                for n in range(1,10):
                    if(test_fit(x, y, n)):
                        board[x][y] = n
                        board = solve_board(board)
                        board[x][y] = 0

                return board


    if(test_board(board)):
        print(board)
        quit()
    return board
        
def test_fit(x, y, number):
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


def test_board(board):
    
    for x in range(9):
        for y in range(9):
            number = board[x][y]
            if number == 0:
                return False
            for i in range(9):
                if number == board[x][i]: 
                    if i == y:
                        continue
                    else:
                        return False
                if number == board[i][y]:
                    if i == x:
                        continue
                    else:
                        return False
            
            xcord = (x // 3) * 3
            ycord = (y // 3) * 3

            for k in range(3):
                for l in range(3):
                    number = board[x][y]
                    if board[xcord+k][ycord+l] == number:
                        if (xcord+k) == x and (ycord+l) == y:
                            continue
    
                        return False

    return True
board = np.zeros((9,9), dtype=int)
board[0] = [6, 4, 9, 2, 5, 7, 1, 8, 3]
# board2 = np.array([
#     [6, 4, 9, 2, 5, 7, 1, 8, 3],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ])

ee = solve_board(board)
print("-----------------------------")
print(board)
print("-----------------------------")
print(final)



# print(test_board(board2))





    

