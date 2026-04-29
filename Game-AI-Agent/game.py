import numpy as np
import random
from config import BOARD_SIZE

def new_game():
    board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    add_tile(board)
    add_tile(board)
    return board

def add_tile(board):
    empty = list(zip(*np.where(board == 0)))
    if empty:
        x, y = random.choice(empty)
        board[x][y] = 2 if random.random() < 0.9 else 4

def compress(row):
    new_row = row[row != 0]
    return np.pad(new_row, (0, BOARD_SIZE - len(new_row)))

def merge(row):
    for i in range(BOARD_SIZE - 1):
        if row[i] == row[i+1] and row[i] != 0:
            row[i] *= 2
            row[i+1] = 0
    return row

def move_left(board):
    new_board = np.zeros_like(board)
    for i in range(BOARD_SIZE):
        row = compress(board[i])
        row = merge(row)
        row = compress(row)
        new_board[i] = row
    return new_board

def rotate(board):
    return np.rot90(board)

def move(board, direction):
    temp = board.copy()
    for _ in range(direction):
        temp = rotate(temp)
    temp = move_left(temp)
    for _ in range((4 - direction) % 4):
        temp = rotate(temp)
    return temp

def valid_moves(board):
    moves = []
    for d in range(4):
        if not np.array_equal(board, move(board, d)):
            moves.append(d)
    return moves