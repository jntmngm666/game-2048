import numpy as np

def evaluate(board):
    empty = np.sum(board == 0)

    mono = 0
    for row in board:
        mono += np.sum(np.diff(row) <= 0)

    max_tile = np.max(board)

    return empty * 100 + mono * 10 + max_tile