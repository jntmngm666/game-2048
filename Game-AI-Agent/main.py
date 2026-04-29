from game import new_game, move, add_tile, valid_moves
from agent import ExpectimaxAgent
from config import SEARCH_DEPTH
import numpy as np

def print_board(board):
    print(board)
    print("Max:", np.max(board))
    print("-" * 20)

def run():
    board = new_game()
    agent = ExpectimaxAgent(depth=SEARCH_DEPTH)

    step = 0
    while True:
        step += 1
        print(f"Step {step}")
        print_board(board)

        moves = valid_moves(board)
        if not moves:
            break

        action = agent.get_action(board)
        board = move(board, action)
        add_tile(board)

    print("Game Over!")
    print_board(board)

if __name__ == "__main__":
    run()