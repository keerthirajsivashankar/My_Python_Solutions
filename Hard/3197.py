import math
from typing import List

class Solution:
  def minimumSum(self, grid: List[List[int]]) -> int:
    """
    Calculates the minimum sum of the areas of three rectangles that enclose
    all the '1's in a binary grid.

    The solution systematically checks all six possible ways to partition the grid
    into three rectangles using two parallel cuts.

    Args:
      grid: A 2D list of integers (0s and 1s).

    Returns:
      The minimum possible sum of the areas.
    """
    m = len(grid)
    n = len(grid[0])
    # Initialize the minimum area with the maximum possible value (full grid area).
    ans = m * n

    # --- Strategy 1: One horizontal cut, then a vertical cut on the top part. ---
    for i in range(m):
      # Calculate the area of the top rectangle [0...i].
      top_area = self._minimumArea(grid, 0, i, 0, n - 1)
      # Iterate through vertical cuts in the remaining bottom part [i+1...m-1].
      for j in range(n):
        ans = min(ans, top_area +
                  # Area of bottom-left rectangle [i+1...m-1, 0...j].
                  self._minimumArea(grid, i + 1, m - 1, 0, j) +
                  # Area of bottom-right rectangle [i+1...m-1, j+1...n-1].
                  self._minimumArea(grid, i + 1, m - 1, j + 1, n - 1))
    
    # --- Strategy 2: One horizontal cut, then a vertical cut on the bottom part. ---
    for i in range(m):
      # Calculate the area of the bottom rectangle [i...m-1].
      bottom_area = self._minimumArea(grid, i, m - 1, 0, n - 1)
      # Iterate through vertical cuts in the remaining top part [0...i-1].
      for j in range(n):
        ans = min(ans, bottom_area +
                  # Area of top-left rectangle [0...i-1, 0...j].
                  self._minimumArea(grid, 0, i - 1, 0, j) +
                  # Area of top-right rectangle [0...i-1, j+1...n-1].
                  self._minimumArea(grid, 0, i - 1, j + 1, n - 1))

    # --- Strategy 3: One vertical cut, then a horizontal cut on the left part. ---
    for j in range(n):
      # Calculate the area of the left rectangle [0...j].
      left_area = self._minimumArea(grid, 0, m - 1, 0, j)
      # Iterate through horizontal cuts in the remaining right part [j+1...n-1].
      for i in range(m):
        ans = min(ans, left_area +
                  # Area of right-top rectangle [0...i, j+1...n-1].
                  self._minimumArea(grid, 0, i, j + 1, n - 1) +
                  # Area of right-bottom rectangle [i+1...m-1, j+1...n-1].
                  self._minimumArea(grid, i + 1, m - 1, j + 1, n - 1))

    # --- Strategy 4: One vertical cut, then a horizontal cut on the right part. ---
    for j in range(n):
      # Calculate the area of the right rectangle [j...n-1].
      right_area = self._minimumArea(grid, 0, m - 1, j, n - 1)
      # Iterate through horizontal cuts in the remaining left part [0...j-1].
      for i in range(m):
        ans = min(ans, right_area +
                  # Area of left-top rectangle [0...i, 0...j-1].
                  self._minimumArea(grid, 0, i, 0, j - 1) +
                  # Area of left-bottom rectangle [i+1...m-1, 0...j-1].
                  self._minimumArea(grid, i + 1, m - 1, 0, j - 1))

    # --- Strategy 5: Two parallel horizontal cuts. ---
    for i1 in range(m):
      for i2 in range(i1 + 1, m):
        ans = min(ans, self._minimumArea(grid, 0, i1, 0, n - 1) +
                  self._minimumArea(grid, i1 + 1, i2, 0, n - 1) +
                  self._minimumArea(grid, i2 + 1, m - 1, 0, n - 1))

    # --- Strategy 6: Two parallel vertical cuts. ---
    for j1 in range(n):
      for j2 in range(j1 + 1, n):
        ans = min(ans, self._minimumArea(grid, 0, m - 1, 0, j1) +
                  self._minimumArea(grid, 0, m - 1, j1 + 1, j2) +
                  self._minimumArea(grid, 0, m - 1, j2 + 1, n - 1))

    return ans

  def _minimumArea(
      self,
      grid: List[List[int]],
      si: int,
      ei: int,
      sj: int,
      ej: int,
  ) -> int:
    """
    Calculates the minimum area of a rectangle enclosing all '1's within
    a specified sub-grid.

    Args:
      grid: The full grid.
      si, ei: Start and end row indices of the sub-grid.
      sj, ej: Start and end column indices of the sub-grid.

    Returns:
      The area of the minimum enclosing rectangle. Returns 0 if no '1's are present.
    """
    x1, y1 = math.inf, math.inf
    x2, y2 = -1, -1

    for i in range(si, ei + 1):
      for j in range(sj, ej + 1):
        if grid[i][j] == 1:
          x1 = min(x1, i)
          y1 = min(y1, j)
          x2 = max(x2, i)
          y2 = max(y2, j)

    # Check if any '1' was found in the sub-grid.
    if x1 == math.inf:
      return 0
    
    # Calculate and return the area.
    return (x2 - x1 + 1) * (y2 - y1 + 1)

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
                if not all(x in [0, 1] for x in row):
                    print("Row must contain only 0s and 1s. Please try again.")
                    continue
                rows.append(row)

            if not rows or all(len(row) == len(rows[0]) for row in rows):
                return rows
            else:
                print("All rows must have the same number of elements.")
        except ValueError:
            print("Invalid input. Please enter 0s and 1s separated by spaces.")

if __name__ == "__main__":
    sol = Solution()
    
    print("--- Minimum Sum of Three Rectangle Areas Finder ---")
    
    matrix_val = get_matrix_input("Enter a binary matrix (0s and 1s) row by row:")
    
    if not matrix_val:
        print("No matrix provided.")
    else:
        result = sol.minimumSum(matrix_val)
        print(f"\nThe minimum sum of the areas of three rectangles is: {result}")
