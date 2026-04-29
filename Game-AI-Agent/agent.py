import numpy as np
from game import move, valid_moves
from utils import evaluate

class ExpectimaxAgent:
    def __init__(self, depth=3):
        self.depth = depth

    def expectimax(self, board, depth, is_player):
        if depth == 0:
            return evaluate(board)

        if is_player:
            best = -float('inf')
            for move_dir in valid_moves(board):
                new_board = move(board, move_dir)
                val = self.expectimax(new_board, depth-1, False)
                best = max(best, val)
            return best
        else:
            empty = list(zip(*np.where(board == 0)))
            if not empty:
                return evaluate(board)

            total = 0
            for x, y in empty:
                for val, prob in [(2, 0.9), (4, 0.1)]:
                    new_board = board.copy()
                    new_board[x][y] = val
                    total += prob * self.expectimax(new_board, depth-1, True)
            return total / len(empty)

    def get_action(self, board):
        best_val = -float('inf')
        best_move = 0

        for move_dir in valid_moves(board):
            new_board = move(board, move_dir)
            val = self.expectimax(new_board, self.depth, False)

            if val > best_val:
                best_val = val
                best_move = move_dir

        return best_move