import math
import itertools
from typing import List

class Solution:
  def judgePoint24(self, nums: List[int]) -> bool:
    """
    Determines if it's possible to get 24 by using all four numbers
    with the four basic arithmetic operations.

    Args:
      nums: A list of four integers.

    Returns:
      True if 24 can be formed, False otherwise.
    """

    def generate(a: float, b: float) -> List[float]:
      """
      Generates all possible results from two numbers using the four
      basic arithmetic operations.
      
      Includes both a/b and b/a, and a-b and b-a, to account for all permutations.
      Division by zero is handled by returning infinity.
      """
      return [a * b,
              b / a if a != 0 else math.inf,
              a / b if b != 0 else math.inf,
              a + b, a - b, b - a]

    def dfs(nums: List[float]) -> bool:
      """
      The core recursive function that uses Depth-First Search to explore all
      possible combinations of operations.
      """
      # Base case: If only one number is left, check if it's approximately 24.
      # We use a small tolerance (0.001) for floating-point comparisons.
      if len(nums) == 1:
        return abs(nums[0] - 24.0) < 0.001

      # Iterate through all unique pairs of numbers using itertools.
      for i, j in itertools.combinations(range(len(nums)), 2):
        # For each pair, generate all possible results of the operations.
        for num in generate(nums[i], nums[j]):
          # Create a new list for the next recursive call.
          # It contains the result of the operation plus the other numbers.
          next_round = [num]
          for k in range(len(nums)):
            # Add the numbers that were NOT part of the operation.
            if k != i and k != j:
              next_round.append(nums[k])
          
          # Recursive call: continue the process with the new list.
          if dfs(next_round):
            return True

      # If no combination works, return False.
      return False

    # Start the DFS with the initial list of numbers.
    # Convert them to floats at the start to prevent integer division issues.
    return dfs([float(n) for n in nums])

# --- Example Usage ---
def get_list_of_integers_input(prompt: str) -> List[int]:
    """Helper function to get a list of 4 integers from the user."""
    while True:
        try:
            input_str = input(prompt)
            elements = [int(x) for x in input_str.split()]
            if len(elements) == 4:
                return elements
            else:
                print("Please enter exactly 4 integers separated by spaces.")
        except ValueError:
            print("Invalid input. Please enter integers only.")

if __name__ == "__main__":
    sol = Solution()
    
    print("--- 24 Game Solver ---")
    
    nums_val = get_list_of_integers_input("Enter four numbers separated by spaces (e.g., 4 1 8 7): ")
    
    result = sol.judgePoint24(nums_val)
    print(f"\nCan the numbers {nums_val} be used to make 24? {result}")

