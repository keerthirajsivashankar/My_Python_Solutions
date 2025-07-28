import functools
import operator
from typing import List

class Solution:
  def countMaxOrSubsets(self, nums: List[int]) -> int:
    # Step 1: Calculate the maximum possible bitwise OR sum (ors).
    # This is achieved by performing a bitwise OR on all elements in nums.
    # Since any bit set in any number will be set in the final OR sum,
    # this gives the maximum possible OR value for any subset.
    ors = functools.reduce(operator.or_, nums)
    
    # Initialize a counter for the number of subsets that achieve this maximum OR sum.
    ans = 0

    # Step 2: Use Depth-First Search (DFS) to explore all subsets.
    # i: the current index in nums being considered.
    # path: the bitwise OR sum of the subset being built so far.
    def dfs(i: int, path: int) -> None:
      nonlocal ans # Declare 'ans' as nonlocal to modify the outer scope's variable.

      # Base case: If we have considered all elements in nums.
      if i == len(nums):
        # If the current subset's OR sum ('path') is equal to the maximum possible OR sum ('ors'),
        # then this subset is one of the "good" subsets.
        if path == ors:
          ans += 1 # Increment the counter.
        return # End recursion for this path.

      # Recursive calls: Explore two possibilities for each element nums[i].

      # Possibility 1: Exclude nums[i] from the current subset.
      # Move to the next element, and the 'path' sum remains unchanged.
      dfs(i + 1, path)
      
      # Possibility 2: Include nums[i] in the current subset.
      # Move to the next element, and update the 'path' sum by ORing it with nums[i].
      dfs(i + 1, path | nums[i])

    # Start the DFS from the beginning of the array (index 0) with an initial OR sum of 0.
    dfs(0, 0)
    
    # Return the total count of subsets that have the maximum OR sum.
    return ans

def get_list_of_integers_input(prompt: str) -> List[int]:
    """
    Prompts the user to enter a list of integers, handles input parsing and validation.
    """
    while True:
        try:
            input_str = input(prompt)
            elements = [int(x) for x in input_str.split()]
            if not elements:
                print("List cannot be empty. Please enter at least one integer.")
            else:
                return elements
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    sol = Solution()
    
    print("--- Count Subsets With Maximum Bitwise OR Sum ---")
    
    # Get the array of numbers from the user
    nums_val = get_list_of_integers_input("Enter numbers for the array separated by spaces (e.g., '3 1 2 4'): ")

    # Call the solution method and print the result
    result = sol.countMaxOrSubsets(nums_val)
    print(f"\nThe number of subsets with the maximum OR sum is: {result}")
