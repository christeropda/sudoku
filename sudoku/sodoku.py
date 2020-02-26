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

def find_missing_numbers_row(board, row, n, skip):
    
    numbers = [1,2,3,4,5,6,7,8,9]

    if skip != -1:
        numbers.pop(skip - 1)

    for i in range(n-1):
        if board[row][i] != 0:
            numbers = find_and_pop(numbers, board[row][i])

    return numbers

def find_and_pop(number_list, number):
    for i in range(len(number_list)):
        if number_list[i] == number:
            number_list.pop(i)
            return number_list

def eval_n(board, number, i, j):
    element = 0
    
    while(element < len(number)):
        if board[i][j] != 0:
            return -1

        if number[element] in board[i,:] or number[element] in board[:,j]:
            print("popped an element, before pop", element, len(number))
            number.pop(element)
            print("popped an element, before pop, after pop", element, len(number))
        
        if element >= len(number):
            print("element > len")
            if len(number) > 0:
                return 1
            else:
                return 0
        

        if number[element] not in board[i,:] and number[element] not in board[:,j]:
                x, y = find_coord(i,j)
                for k in range(3):
                    for l in range(3):
                        try:
                            if board[x+k][y+l] == number[element]:
                                number.pop(element)
                        except:
                            print(x+k, y+l, element, len(number))
        
        element += 1
    
    if len(number) == 0:
        return 0
    
    return 1

def fill_cell(board, i, j, options):
    if len(options) == 0:
        print("hoihojfowjef")
        return
    
    status = eval_n(board, options, i, j)
    
    if status == 0:
        print("no numbers left in options")
        return status

    if status == -1:
        print("number wasnt 0")
        return status

    if status == 1:
        print("all is well, added")  
        index = randint(0, len(options)-1)
        board[i][j] = options[index]
        options.pop(index)
        return status
    
    


def create_board(n):
    board = np.zeros((n,n), dtype=int)
    # board = np.array([
    #     [0,0,3,0,2,0,6,0,0],
    #     [9,0,0,3,0,5,0,0,1],
    #     [0,0,1,8,0,6,4,0,0],
    #     [0,0,8,1,0,2,9,0,0],
    #     [7,0,0,0,0,0,0,0,8],
    #     [0,0,6,7,0,8,2,0,0],
    #     [0,0,2,6,0,9,5,0,0],
    #     [8,0,0,2,0,3,0,0,9],
    #     [0,0,5,0,1,0,3,0,0]
    # ])
    number_to_skip = -1
    
    i = 0
    j = 0
    while(i < n):
        while(j < n):
            options = find_missing_numbers_row(board, i, n, number_to_skip)
            number_to_skip = -1
            status = fill_cell(board, (i), (j), options)
            
            print(board)
            time.sleep(1)
            
            if status == 1:
                j += 1
                if j > (n-1):
                    j = 0
                    i = i+1
                
                    options = [1,2,3,4,5,6,7,8,9]
                
                continue
            
            if status == -1:
                if len(options) > 0:
                    j += 1
                    break
                if j > (n-1):
                    j = 0
                    i += 1
                    break
                else:
                    board[i][j] = 0
                    j = j-1
                    number_to_skip = board[i][j]
                    board[i][j] = 0
                
                    break
                print("gikk gjennom alle tester uten å gjøre noe, status -1")
            
            if len(options) == 0:
                if status == 1:
                    if j == (n-1):
                        j = 0
                        i = i+1
                    
                        options = [1,2,3,4,5,6,7,8,9]
                    
                    break
                
                if status == 0:
                    #ensure current j is 0 go back one and reset that to zero
                    board[i][j] = 0
                    j = j-1
                    number_to_skip = board[i][j]
                    board[i][j] = 0
                    break

                print("gikk gjennom alle tester uten å gjøre noe, len 0")
                
            


        
    
    return board

                    
s = create_board(9)
print(s)

