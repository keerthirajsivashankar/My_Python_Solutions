import heapq
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves a Sudoku puzzle using a backtracking algorithm with an
        optimization to fill the easiest cells first.
        """
        # Data structures to keep track of numbers used in each row, column, and 3x3 grid.
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [[set() for _ in range(3)] for _ in range(3)]
        
        # List to store the coordinates of empty cells.
        empty_cells = []
        
        # First pass: populate the sets and identify all empty cells.
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value == ".":
                    empty_cells.append((i, j))
                else:
                    rows[i].add(value)
                    cols[j].add(value)
                    grids[i // 3][j // 3].add(value)
        
        # Optimization: create a min-heap of empty cells, prioritized by the number
        # of potential numbers they can hold.
        # This helps the algorithm fill the most constrained cells first.
        empty_cells_with_priority = [
            (9 - len(rows[i] | cols[j] | grids[i // 3][j // 3]), i, j)
            for i, j in empty_cells
        ]
        heapq.heapify(empty_cells_with_priority)

        def fill_board() -> bool:
            """
            Recursive backtracking function to fill the empty cells.
            """
            # Base case: if there are no more empty cells, the board is solved.
            if not empty_cells_with_priority:
                return True

            # Get the cell with the fewest potential numbers from the min-heap.
            _, i, j = heapq.heappop(empty_cells_with_priority)
            
            row_set = rows[i]
            col_set = cols[j]
            grid_set = grids[i // 3][j // 3]

            # Try placing a number from '1' to '9' in the current empty cell.
            for value in '123456789':
                # Check if the number is already present in the row, column, or grid.
                if value in row_set or value in col_set or value in grid_set:
                    continue

                # If the number is valid, place it on the board and in the sets.
                board[i][j] = value
                row_set.add(value)
                col_set.add(value)
                grid_set.add(value)

                # Recursively try to fill the rest of the board.
                if fill_board():
                    return True

                # If the recursive call failed (meaning this number didn't lead to a solution),
                # backtrack by removing the number from the board and the sets.
                row_set.remove(value)
                col_set.remove(value)
                grid_set.remove(value)
            
            # If no number from '1' to '9' can be placed, return False.
            # Push the cell back onto the heap so the next recursive call can try again.
            heapq.heappush(empty_cells_with_priority, (9 - len(row_set | col_set | grid_set), i, j))
            
            return False
            
        # Start the solving process.
        fill_board()


if __name__ == "__main__":
    sol = Solution()
    
    # A sample Sudoku board to test the solver.
    # The '.' characters represent empty cells.
    sudoku_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    print("--- Unsolved Sudoku Board ---")
    for row in sudoku_board:
        print(" ".join(row))

    sol.solveSudoku(sudoku_board)

    print("\n--- Solved Sudoku Board ---")
    for row in sudoku_board:
        print(" ".join(row))
