import bisect
from typing import List

class Solution:
  def minimizeMax(self, nums: List[int], p: int) -> int:
    nums.sort()

    def numPairs(maxDiff: int) -> int:
      pairs = 0
      i = 1
      while i < len(nums):
        if nums[i] - nums[i - 1] <= maxDiff:
          pairs += 1
          i += 2
        else:
          i += 1
      return pairs

    return bisect.bisect_left(range(nums[-1] - nums[0]), p, key=numPairs)

def get_list_of_integers_input(prompt: str) -> List[int]:
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

def get_integer_input(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    sol = Solution()
    
    nums_val = get_list_of_integers_input("Enter numbers separated by spaces (e.g., '10 1 2 7 1 3'): ")
    p_val = get_integer_input("Enter the target number of pairs (p): ")

    result = sol.minimizeMax(nums_val, p_val)
    print(f"The minimized maximum difference is: {result}")