def is_valid(board, row, col, num):
    # Check if the number is not in the given row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number is not in the given column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is not in the 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve(board):
    # Find the first empty cell (denoted by 0)
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try all numbers from 1 to 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Place the number
                        # Recursively attempt to solve with the new number
                        if solve(board):
                            return True
                        # If it doesn't work, backtrack (reset the cell)
                        board[row][col] = 0
                return False  # If no number works, backtrack
    return True  # If the entire board is filled, return True

def print_board(board):
    for row in board:
        print(row)

# Input Sudoku puzzle (partially filled with 0's)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku puzzle
if solve(board):
    print("Solved Sudoku:")
    print_board(board)
else:
    print("No solution exists.")
