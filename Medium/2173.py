import sys
from typing import List

class Solution:
  def countSquares(self, matrix: List[List[int]]) -> int:
    """
    Counts the number of square submatrices with all ones using dynamic programming.
    This solution modifies the input matrix in place to store the size of the largest
    square with its bottom-right corner at each cell.

    Args:
      matrix: A 2D list of integers (0s and 1s).

    Returns:
      The total number of square submatrices with all ones.
    """
    # Iterate through the matrix starting from the second row and column.
    # The first row and column are the base cases, as a square can only
    # have a size of 1 there.
    for i in range(1, len(matrix)):
      for j in range(1, len(matrix[0])):
        # If the current cell is a 1, it can be the bottom-right corner of a square.
        if matrix[i][j] == 1:
          # The size of the largest square ending at (i, j) is 1 plus the
          # minimum of the sizes of the squares at its top, top-left, and left.
          # This is because a new square can only be formed if all three
          # adjacent cells are part of existing squares.
          matrix[i][j] += min(matrix[i - 1][j - 1],
                              matrix[i - 1][j], 
                              matrix[i][j - 1])
    
    # The total number of squares is the sum of all values in the modified matrix.
    # A cell with value 'k' means there are k squares ending at that position
    # (of sizes 1, 2, ..., k). Summing these up gives the total count.
    return sum(map(sum, matrix))

# --- Example Usage ---
def get_matrix_input(prompt: str) -> List[List[int]]:
    """Helper function to get a binary matrix from the user."""
    while True:
        try:
            print(prompt)
            rows = []
            while True:
                row_str = input("Enter a row (e.g., '1 0 1') or leave empty to finish: ")
                if not row_str:
                    break
                row = [int(x) for x in row_str.split()]
                # Basic validation: ensure elements are 0 or 1
                if not all(x in [0, 1] for x in row):
                    print("Row must contain only 0s and 1s. Please try again.")
                    continue
                rows.append(row)

            # Check if all rows have the same length
            if not rows or all(len(row) == len(rows[0]) for row in rows):
                return rows
            else:
                print("All rows must have the same number of elements.")
        except ValueError:
            print("Invalid input. Please enter 0s and 1s separated by spaces.")

if __name__ == "__main__":
    sol = Solution()
    
    print("--- Square Submatrix Counter ---")
    
    matrix_val = get_matrix_input("Enter a binary matrix (0s and 1s) row by row:")
    
    if not matrix_val:
        print("No matrix provided.")
    else:
        result = sol.countSquares(matrix_val)
        print(f"\nFor the given matrix, the total number of squares is: {result}")
