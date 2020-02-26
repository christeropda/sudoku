import numpy as np
import time
from random import randint

def find_coord(i, j):
    if i < 3:
        x = 0
        if j < 3:
            y = 0
        elif j < 6:
            y = 3
        else:
            y = 6
    elif i < 6:
        x = 3
        if j < 3:
            y = 0
        elif j < 6:
            y = 3
        else:
            y = 6
    else:
        x = 6
        if j < 3:
            y = 0
        elif j < 6:
            y = 3
        else:
            y = 6                 
    return x, y

def check_cells(board, i, j):
    options = []
    number = 1
    
    while(j < 9):
        skip = False
        if number not in board[i] and number not in board[:,j]:
            x, y = find_coord(i,j)
            for k in range(3):
                for l in range(3):
                    if board[x+k][y+l] == number:
                        skip = True
                        break
            
            if skip == False:
                options.append(number)
                print("apend", number)
        
        number += 1
        j += 1

    return options

def eval_n(board, number, i, j):
    if board[i][j] != 0:
        return -1

    if number in board[i,:] or number in board[:,j]:
        return 0

    if number not in board[i,:] and number not in board[:,j]:
            x, y = find_coord(i,j)
            for k in range(3):
                for l in range(3):
                    if board[x+k][y+l] == number:
                        return 0
    
    return 1

def fill_cell(board, i, j, options):
    if len(options) == 0:
        print("hoihojfowjef")
        return -1
    
    index = randint(0, len(options)-1)
    number = options[index]
    
    if(eval_n(board, number, i, j) == 0):
        print("not ok, recursion", number)
        options.pop(index) 
        fill_cell(board, i, j, options)
        return 0

    if(eval_n(board, number, i, j) == -1):
        return 1

    else:
        print("all is well, added", number)  
        board[i][j] = number
        options.pop(index)
        return 1
    
    


def create_board(options, n):
    #1,1    1,3     1,6
    #3,1    3,3     3,6
    #6,1    6,3     6,6 

    i = 0
    j = 0
    
    board = np.zeros((n,n), dtype=int)
    
    while(i < n):
        while(j < n):
            status = fill_cell(board, (i%n), (j%n), options)
            print(board)
            time.sleep(1)
            print(status)
            if len(options) == 0 and status != -1:
                if j == (n-1):
                    j = 0
                    i = i+1
                    options = [1,2,3,4,5,6,7,8,9]
                    break

                elif status == 0 or status == -1:
                    j = j-1
                    board[i][j] = 0
                    options = check_cells(board, i, j)
                
                else:
                    print("j", j)
                    options = check_cells(board, i, j)
        
           
            #gå videre
            if status == 1:
                j += 1

        #ikke inkrementer om flagget er false
        
        #gå videre
        #i += 1
        
    
    return board

                    

options = [1,2,3,4,5,6,7,8,9]
s = create_board(options, 9)
print(s)

