import numpy as np
import random
import time
import matplotlib.pyplot as plt

def create_board():
    return np.zeros((3,3), dtype=int)
    
def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        
def possibilities(board):
    not_occupied = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                not_occupied.append((i,j))
    return not_occupied

def random_place(board, player):
    position = random.choice(possibilities(board))
    place(board, player, position)
   # return board # not sure why is needed to return board

def row_win(board, player):
    map1 = map(lambda row: all(list(map(lambda playerNum: playerNum == player, row))), board)
    return any(list(map1))

def col_win(board, player):
    return row_win(np.transpose(board), player)

def diag_win(board, player):
    diags = [[],[]]
    n = len(board)
    for i in range(n):
        diags[0].append(board[i][i])
        diags[1].append(board[i][n-i-1])
            
    m = map(lambda row: all(list(map(lambda playerNum: playerNum == player, row))), diags)
    return any(list(m))

def evaluate(board):
    result = 0
    
    for player in [1,2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            return player
    
    if len(possibilities(board)) == 0:
        result = -1
        
    return result

def play_game(strat):
    board = create_board()
    result = 0
    counter = 0
    
    if strat:
        place(board, 1, (1,1))
        counter += 1
        
    while result == 0:
        random_place(board, counter % 2 + 1)
        result = evaluate(board)
        counter += 1

    return result

    
start = time.time()
results = [[],[]]
for i in range(10000):
    results[0].append(play_game(False))
    results[1].append(play_game(True))
    
plt.hist(results)

stop = time.time()
print(stop - start)
