#!/usr/bin/python3
"""nqueens module"""
import sys

# check the number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# get N from the command-line argument
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# check that N is at least 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)


def can_place(board, r, c):
    """helper function to check if a queen can be placed at row r and column c
    """
    for i in range(r):
        # check if there is a queen in the same column or diagonal
        if board[i] == c or board[i] - i == c - r or board[i] + i == c + r:
            return False
    return True


def place_queens(board, r, solutions):
    """recursive function to place queens on the board"""
    # base case: all queens have been placed
    if r == N:
        solutions.append(board[:])
    else:
        for c in range(N):
            if can_place(board, r, c):
                board[r] = c
                place_queens(board, r+1, solutions)


# create an empty board
board = [0] * N

# find all solutions
solutions = []
place_queens(board, 0, solutions)

# print solutions
for solution in solutions:
    print(" ".join(str(x+1) for x in solution))
