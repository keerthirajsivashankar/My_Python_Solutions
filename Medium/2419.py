from typing import List

class Solution:
  def longestSubarray(self, nums: List[int]) -> int:
    ans = 0 # Stores the maximum length of the subarray found so far
    maxIndex = 0 # Stores the index of the current maximum element encountered
    sameNumLength = 0 # Stores the length of the current subarray of identical elements
                      # that are equal to nums[maxIndex]

    # Iterate through the array with both index (i) and value (num)
    for i, num in enumerate(nums):
      # Case 1: The current number is equal to the current maximum number found
      if nums[i] == nums[maxIndex]:
        sameNumLength += 1 # Extend the current sequence of identical maximum numbers
        ans = max(ans, sameNumLength) # Update the overall maximum length
      # Case 2: The current number is greater than the current maximum number
      elif nums[i] > nums[maxIndex]:
        maxIndex = i # Update the index of the new maximum number
        sameNumLength = 1 # Reset the length, as this is a new sequence starting here
        ans = 1 # The longest subarray is now at least 1 (the current number itself)
      # Case 3: The current number is smaller than the current maximum number
      else:
        # The sequence of maximum numbers is broken, reset its length
        sameNumLength = 0 

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
    
    print("--- Longest Subarray of Maximum Element ---")
    
    # Get the array of numbers from the user
    nums_val = get_list_of_integers_input("Enter numbers for the array (e.g., '1 2 2 3 3 3 2 4 4'): ")

    # Call the solution method and print the result
    result = sol.longestSubarray(nums_val)
    print(f"\nThe length of the longest subarray containing only the maximum element is: {result}")