import itertools
import ast

class Solution:
  """
  A class to solve the "Maximum Total Fruits" problem.
  The problem is to find the maximum number of fruits you can collect
  starting from a given position, with a maximum number of steps `k`.
  """
  def maxTotalFruits(
      self,
      fruits: list[list[int]],
      startPos: int,
      k: int,
  ) -> int:
    """
    Calculates the maximum number of fruits that can be collected.

    Args:
      fruits: A list of lists, where each inner list [position, amount]
              represents the position and amount of fruits at that spot.
      startPos: The starting position.
      k: The maximum number of steps you can take.

    Returns:
      The maximum number of fruits that can be collected.
    """
    ans = 0

    # Determine the maximum possible position to create a comprehensive `amounts` array.
    # The max position is either the starting position or the last fruit's position.
    maxRight = max(startPos, fruits[-1][0]) if fruits else startPos
    
    # Create an array to store the amount of fruits at each position.
    amounts = [0] * (1 + maxRight)
    for position, amount in fruits:
      if 0 <= position <= maxRight:
          amounts[position] = amount
    
    # Create a prefix sum array for efficient range sum queries.
    prefix = list(itertools.accumulate(amounts, initial=0))

    def getFruits(leftSteps: int, rightSteps: int) -> int:
      """
      Helper function to get the sum of fruits within a given range.
      """
      l = max(0, startPos - leftSteps)
      r = min(maxRight, startPos + rightSteps)
      return prefix[r + 1] - prefix[l]

    # Strategy 1: Go right first, then turn left.
    # The `rightSteps` can range from 0 to k, but also limited by the max position.
    for rightSteps in range(min(maxRight - startPos, k) + 1):
      # Calculate remaining steps after going right.
      remaining_steps = k - rightSteps
      # To turn left, we need to go back `rightSteps` and then some.
      # The total distance left is k - 2 * rightSteps.
      leftSteps = max(0, remaining_steps - rightSteps)
      ans = max(ans, getFruits(leftSteps, rightSteps))

    # Strategy 2: Go left first, then turn right.
    # The `leftSteps` can range from 0 to k, but also limited by the start position.
    for leftSteps in range(min(startPos, k) + 1):
      # Calculate remaining steps after going left.
      remaining_steps = k - leftSteps
      # To turn right, we need to go back `leftSteps` and then some.
      # The total distance right is k - 2 * leftSteps.
      rightSteps = max(0, remaining_steps - leftSteps)
      ans = max(ans, getFruits(leftSteps, rightSteps))

    return ans

if __name__ == "__main__":
  try:
    # Example usage with user input
    fruits_input = input("Enter fruits as a list of lists (e.g., [[2,8],[6,3],[8,6]]): ")
    # Use ast.literal_eval for safe parsing of the list of lists.
    fruits = ast.literal_eval(fruits_input)
    
    startPos = int(input("Enter the starting position (e.g., 5): "))
    k = int(input("Enter the maximum steps k (e.g., 7): "))

    # Instantiate the Solution class and call the method
    solution = Solution()
    result = solution.maxTotalFruits(fruits, startPos, k)

    print(f"The maximum number of fruits you can collect is: {result}")

  except (ValueError, SyntaxError) as e:
    print(f"Invalid input: {e}")
    print("Please ensure your input is in the correct format.")

