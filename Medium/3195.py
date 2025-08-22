import math
from typing import List

class Solution:
  def minimumArea(self, grid: List[List[int]]) -> int:
    """
    Calculates the minimum area of a rectangle that encloses all '1's
    in a binary grid.

    This is achieved by finding the top-most, left-most, bottom-most,
    and right-most coordinates of all '1's to form the smallest
    possible bounding box.

    Args:
      grid: A 2D list of integers (0s and 1s).

    Returns:
      The area of the minimum enclosing rectangle. Returns 0 if no '1's are present.
    """
    # Initialize boundary coordinates.
    # We use math.inf for min values to ensure the first '1' found
    # will correctly set the initial boundaries.
    x1, y1 = math.inf, math.inf
    x2, y2 = 0, 0

    # Iterate through the grid to find the boundaries of the '1's.
    for i, row in enumerate(grid):
      for j, num in enumerate(row):
        if num == 1:
          # If we find a '1', update the boundary coordinates.
          x1 = min(i, x1) # Update top boundary
          y1 = min(j, y1) # Update left boundary
          x2 = max(i, x2) # Update bottom boundary
          y2 = max(j, y2) # Update right boundary
    
    # If no '1's were found, the boundaries will be at their initial values.
    # The area will be zero, which is the correct result.
    if x1 == math.inf:
      return 0
    
    # Calculate the width and height of the bounding box.
    # Width = (right_boundary - left_boundary + 1)
    # Height = (bottom_boundary - top_boundary + 1)
    width = y2 - y1 + 1
    height = x2 - x1 + 1
    
    # Return the product of width and height.
    return width * height

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
    
    print("--- Minimum Area Rectangle Finder ---")
    
    matrix_val = get_matrix_input("Enter a binary matrix (0s and 1s) row by row:")
    
    if not matrix_val:
        print("No matrix provided.")
    else:
        result = sol.minimumArea(matrix_val)
        print(f"\nThe minimum area of a rectangle enclosing all '1's is: {result}")
