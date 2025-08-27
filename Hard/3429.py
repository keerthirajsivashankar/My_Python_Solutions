import functools
import sys
from typing import List

class Solution:
  def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
    """
    Finds the length of the longest "V" shaped path of alternating 1s and 2s
    in a grid, where a "V" is formed by two diagonal segments.

    Args:
      grid: A 2D list of integers.

    Returns:
      The maximum length of a valid V-shaped path.
    """
    m, n = len(grid), len(grid[0])
    
    # DIRS represents the four diagonal directions:
    # (up-right, down-right, down-left, up-left)
    DIRS = ((-1, 1), (1, 1), (1, -1), (-1, -1))

    @functools.lru_cache(None)
    def dfs(i: int, j: int, turned: bool, num: int, dir: int) -> int:
      """
      Performs a depth-first search to find the length of a diagonal path.
      
      Args:
        i, j: The current row and column indices.
        turned: True if a turn has been made; False otherwise.
        num: The number we are currently looking for (1 or 2).
        dir: The current direction index from the DIRS tuple.
      
      Returns:
        The length of the path from this point.
      """
      # Base Case 1: Out of bounds. The path ends.
      if not (0 <= i < m and 0 <= j < n):
        return 0
      # Base Case 2: The number in the grid does not match the one we are looking for.
      if grid[i][j] != num:
        return 0

      # The number we will look for next is the opposite of the current one.
      # The problem implies we alternate between 1 and 2.
      nextNum = 1 if num == 2 else 2
      
      # Get the change in coordinates for the current direction.
      dx, dy = DIRS[dir]
      
      # The length of the current path is 1 (for the current cell) + the length of
      # the path continuing straight.
      res = 1 + dfs(i + dx, j + dy, turned, nextNum, dir)

      # If we haven't turned yet, we can try making a turn.
      if not turned:
        # A turn is simply a new diagonal direction from the current spot.
        # We try all other 3 directions by iterating over DIRS.
        # This is simplified in the user's code by just trying the next direction in the tuple.
        next_dir = (dir + 1) % 4
        next_dx, next_dy = DIRS[next_dir]
        
        # Calculate the length of the path after making a turn.
        # The 'turned' flag is set to True to prevent subsequent turns.
        res = max(res, 1 + dfs(i + next_dx, j + next_dy, True, nextNum, next_dir))

      return res

    # The main part of the solution. We iterate through every cell in the grid.
    # We start a DFS only if the cell contains a '1'.
    return max((dfs(i, j, False, 1, d)
                for i in range(m)
                for j in range(n)
                if grid[i][j] == 1
                for d in range(4)),
               default=0)

# --- Example Usage ---
def get_grid_input(prompt: str) -> List[List[int]]:
    """Helper function to get a matrix from the user."""
    while True:
        try:
            print(prompt)
            rows = []
            while True:
                row_str = input("Enter a row of integers (e.g., '1 2 1 2') or leave empty to finish: ")
                if not row_str:
                    break
                row = [int(x) for x in row_str.split()]
                if not all(x in [1, 2] for x in row):
                    print("Row must contain only 1s and 2s. Please try again.")
                    continue
                rows.append(row)

            if not rows or all(len(row) == len(rows[0]) for row in rows):
                return rows
            else:
                print("All rows must have the same number of elements.")
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")

if __name__ == "__main__":
    solution = Solution()
    
    print("--- Longest V-Shaped Diagonal Finder ---")
    
    grid_val = get_grid_input("Enter a grid of 1s and 2s row by row:")
    
    if not grid_val:
        print("No grid provided.")
    else:
        result = solution.lenOfVDiagonal(grid_val)
        print(f"\nThe length of the longest V-shaped diagonal is: {result}")
