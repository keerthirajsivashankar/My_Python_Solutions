import sys
import ast

class Solution:
    def maxCollectedFruits(self, fruits: list[list[int]]) -> int:
        """
        Solves the "Cherry Pickup II" style problem on a grid.
        Two collectors start at the top corners (0, 0) and (0, n-1)
        and move downwards to the last row, collecting the maximum number of fruits.

        The collectors can move to three possible cells in the next row:
        - Down-left
        - Down
        - Down-right
        
        A dynamic programming approach is used to keep track of the maximum fruits
        collected at each state (row, column1, column2).

        Args:
          fruits: A 2D list of integers representing the grid of fruits.

        Returns:
          The maximum total number of fruits that can be collected by both collectors.
        """
        if not fruits or not fruits[0]:
            return 0
            
        rows = len(fruits)
        cols = len(fruits[0])

        # dp[r][c1][c2] stores the max fruits collected when the two collectors
        # are at row `r` and columns `c1` and `c2` respectively.
        # Initialize with -1 to signify an unreachable state.
        dp = [[[-1] * cols for _ in range(cols)] for _ in range(rows)]
        
        # Base Case: At the first row (row 0), the collectors start at (0, 0) and (0, cols-1).
        # We collect the fruits from their starting positions.
        dp[0][0][cols - 1] = fruits[0][0] + fruits[0][cols - 1]

        # Iterate through the grid, row by row, from the second row onwards.
        for r in range(1, rows):
            # Iterate through all possible column positions for the first collector.
            for c1 in range(cols):
                # Iterate through all possible column positions for the second collector.
                for c2 in range(cols):
                    # Only consider states that were reachable in the previous row.
                    if dp[r - 1][c1][c2] != -1:
                        # Explore all possible moves for both collectors.
                        # Person 1 can move from c1 to c1+dc1
                        for dc1 in [-1, 0, 1]:
                            # Person 2 can move from c2 to c2+dc2
                            for dc2 in [-1, 0, 1]:
                                new_c1 = c1 + dc1
                                new_c2 = c2 + dc2

                                # Check for valid next columns for both collectors.
                                if 0 <= new_c1 < cols and 0 <= new_c2 < cols:
                                    
                                    # Calculate fruits from the current cells.
                                    current_fruits = fruits[r][new_c1]
                                    
                                    # If collectors are not on the same cell, add the second fruit.
                                    # This is a key rule of the problem.
                                    if new_c1 != new_c2:
                                        current_fruits += fruits[r][new_c2]

                                    # Update the DP state for the new position.
                                    # We take the maximum of the current fruits plus the max from the previous state.
                                    dp[r][new_c1][new_c2] = max(
                                        dp[r][new_c1][new_c2],
                                        dp[r - 1][c1][c2] + current_fruits
                                    )

        # Find the maximum value in the last row of the dp table.
        # This represents the maximum fruits collected on any path to the last row.
        max_fruits = 0
        for c1 in range(cols):
            for c2 in range(cols):
                max_fruits = max(max_fruits, dp[rows - 1][c1][c2])
        
        return max_fruits

# Example usage with user input
if __name__ == "__main__":
    try:
        print("This program solves a 'Cherry Pickup II' style problem.")
        print("Please enter the fruit grid as a list of lists.")
        print("Example: [[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], ...]")
        fruits_input = input("Enter the fruit grid: ")
        
        # Safely parse the input string into a Python list of lists.
        fruits_grid = ast.literal_eval(fruits_input)
        
        solution = Solution()
        result = solution.maxCollectedFruits(fruits_grid)
        
        print(f"The maximum number of fruits that can be collected is: {result}")
        
    except (ValueError, SyntaxError) as e:
        print(f"Invalid input: {e}")
        print("Please ensure your input is a valid Python list of lists of integers.")

