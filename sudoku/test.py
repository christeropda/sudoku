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

global board
board = np.empty((9,9), dtype=int)
# board = np.array([
#     [9, 0, 0, 6, 5, 3, 0, 0, 2],
#     [6, 0, 0, 0, 0, 4, 3, 0, 0],
#     [5, 0, 3, 2, 8, 0, 6, 0, 7],
#     [1, 0, 4, 0, 0, 0, 9, 0, 0],
#     [3, 0, 9, 4, 0, 8, 0, 7, 0],
#     [2, 7, 8, 0, 3, 0, 4, 0, 0],
#     [8, 0, 0, 0, 4, 6, 0, 0, 9],
#     [7, 0, 6, 0, 1, 0, 0, 0, 4],
#     [4, 3, 1, 7, 9, 0, 0, 0, 6]
#     ])

def check_board():
  for row in range(0,9):
      for col in range(0,9):
        if board[row][col] == 0:
          return False

def solve_board():  
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                for n in range(1,10):
                    if(test_fit(x, y, n)):
                        board[x][y] = n
                        solve_board()
                        board[x][y] = 0
                return
    print(board)
    input("wpoej")
    


    # if check_board(board) == False:
    #     board[x][y] = 0
        #print(board)
        #time.sleep(0.5)
    #return board
        
def test_fit(x, y, number):
    for i in range(0,9):
        if board[x][i] == number:
            return False
    
    for j in range(0,9):
        if board[j][y] == number:
            return False
    
    xcord = (x // 3) * 3
    ycord = (y // 3) * 3

    for k in range(0,3):
        for l in range(0, 3):
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
# board = np.zeros((9,9), dtype=int)
# board[0] = [6, 4, 9, 2, 5, 7, 1, 8, 3]

solve_board()







    

