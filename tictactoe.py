# Tictactoe: 3x3, xo,
# 1. Given a board & next player, make a random valid move
# 2. Find a winning move. If there is no winning moves, make a random move
# If the board is full, print "No moves"

# [[x, x, -],
#  [-, o, -],
#  [-, -, o],
# ],
# x
from random import random
import math
import unittest


def is_winning(board, next_player):
    # return true if the player wins
    winning_lines = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[2, 0], [1, 1], [0, 2]],
    ]

    for line in winning_lines:
        winning = True
        for cord in line:
            if board[cord[0]][cord[1]] != next_player:
                winning = False
                break
        if winning:
            return True

    return False


def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                return False
    return True


def find_winning_move(board, next_player):
    # try to find a winning move
    for row in range(3):
        for col in range(3):
            if board[row][col] == "-":
                board[row][col] = next_player
                if is_winning(board, next_player):
                    board[row][col] = "-"
                    return [row, col]
                board[row][col] = "-"
    return None


def find_random_move(board, next_player):
    # find a random move
    if is_board_full(board):
        return None

    found = False
    while not found:
        row = math.floor(random() * 3)
        col = math.floor(random() * 3)
        if board[row][col] == "-":
            found = True

    return [row, col]


def find_next_move(board, next_player):
    # next_player could be 'x' or 'o'
    if is_board_full(board):
        return None

    winning_move = find_winning_move(board, next_player)
    if winning_move:
        return winning_move

    random_move = find_random_move(board, next_player)
    if random_move:
        return random_move


class TestTicTacToe(unittest.TestCase):
    def test_winning_board(self):
        winning_board_row = [
            ["x", "x", "-"],
            ["-", "o", "-"],
            ["x", "x", "x"],
        ]

        self.assertEqual(is_winning(winning_board_row, "x"), True,
                         "Should be True")

        winning_board_diagonal = [
            ["x", "x", "-"],
            ["-", "x", "-"],
            ["x", "o", "x"],
        ]

        self.assertEqual(is_winning(winning_board_diagonal, "x"), True,
                         "Should be True")

        not_winning_board = [
            ["x", "-", "-"],
            ["-", "o", "-"],
            ["-", "-", "o"],
        ]
        self.assertEqual(is_winning(not_winning_board, "x"), False,
                         "Should be False")

    def test_full_board(self):
        full_board = [
            ["x", "x", "o"],
            ["x", "o", "x"],
            ["o", "x", "o"],
        ]
        self.assertEqual(is_board_full(full_board), True,
                         "Should be True")

        not_full_board = [
            ["x", "x", "o"],
            ["x", "-", "x"],
            ["o", "x", "o"],
        ]
        self.assertEqual(is_board_full(not_full_board), False,
                         "Should be False")

    def test_winning_move(self):
        winning_move_board_x = [
            ["x", "x", "-"],
            ["o", "-", "-"],
            ["o", "-", "-"],
        ]
        winning_move = find_winning_move(winning_move_board_x, "x")
        self.assertEqual(winning_move, [0, 2], "winning move at [0, 2] for x")

        not_winning_move_board_x = [
            ["x", "-", "-"],
            ["-", "-", "x"],
            ["o", "-", "o"],
        ]
        winning_move = find_winning_move(not_winning_move_board_x, "x")
        self.assertEqual(winning_move, None, "could not find a winning move for x")

        winning_move_board_o = [
            ["x", "-", "-"],
            ["-", "-", "x"],
            ["o", "-", "o"],
        ]
        winning_move = find_winning_move(winning_move_board_o, "o")
        self.assertEqual(winning_move, [2, 1], "a winning move at [2, 1] for o")

    def test_random_move(self):
        full_board = [
            ["x", "x", "o"],
            ["x", "o", "x"],
            ["o", "x", "o"],
        ]
        self.assertEqual(find_random_move(full_board, "x"), None,
                         "Board is full, couldn't find a random move")

        not_full_board = [
            ["x", "x", "o"],
            ["x", "-", "x"],
            ["o", "x", "o"],
        ]

        next_move = find_random_move(not_full_board, "x")
        self.assertEqual(not_full_board[next_move[0]][next_move[1]], "-",
                         "the position at next_move could be played")

    def test_next_move(self):
        full_board = [
            ["x", "x", "o"],
            ["x", "o", "x"],
            ["o", "x", "o"],
        ]

        self.assertEqual(find_next_move(full_board, "x"), None,
                         "Board is full, couldn't find a next move")

        not_full_board = [
            ["x", "x", "o"],
            ["x", "-", "x"],
            ["o", "x", "o"],
        ]

        next_move = find_next_move(not_full_board, "x")
        self.assertEqual(not_full_board[next_move[0]][next_move[1]], "-",
                         "the position at next_move could be played")

        board_with_winning_move = [
            ["x", "x", "-"],
            ["-", "-", "x"],
            ["o", "-", "o"],
        ]

        next_move = find_next_move(board_with_winning_move, "o")
        self.assertEqual(board_with_winning_move[next_move[0]][next_move[1]],
                         "-", "the position at next_move could be played")
        self.assertEqual(next_move, [2, 1],
                         "the position at [2,1] gives a winning move")

                         
if __name__ == "__main__":
    unittest.main()
