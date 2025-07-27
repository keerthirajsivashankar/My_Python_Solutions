from typing import List

class Solution:
  def countHillValley(self, nums: List[int]) -> int:
    ans = 0
    # 'left' tracks the last *distinct* number encountered before nums[i]
    # It starts with the first element of the array.
    left = nums[0]

    # Iterate through the array from the second element up to the second-to-last element.
    # We need to look at nums[i-1] (implicitly 'left'), nums[i], and nums[i+1].
    for i in range(1, len(nums) - 1):
      # Check for a 'hill':
      # nums[i] is greater than the last distinct number to its left ('left')
      # AND nums[i] is greater than the next number to its right (nums[i+1])
      if (left < nums[i] and nums[i] > nums[i + 1] or
          # Check for a 'valley':
          # nums[i] is less than the last distinct number to its left ('left')
          # AND nums[i] is less than the next number to its right (nums[i+1])
          left > nums[i] and nums[i] < nums[i + 1]):
        ans += 1       # Increment the count of hills/valleys
        left = nums[i] # Update 'left' to the current number, as it is now a distinct peak/valley

    return ans

def get_list_of_integers_input(prompt: str) -> List[int]:
    """
    Prompts the user to enter a list of integers, handles input parsing and validation.
    """
    while True:
        try:
            input_str = input(prompt)
            elements = [int(x) for x in input_str.split()]
            if len(elements) < 3: # Minimum 3 elements needed for hills/valleys
                print("Please enter at least 3 integers for the array.")
            else:
                return elements
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    sol = Solution()
    
    print("--- Count Hills and Valleys in an Array ---")
    
    # Get the array of numbers from the user
    nums_val = get_list_of_integers_input("Enter numbers for the array (e.g., '2 4 1 3 2 5'): ")

    # Call the solution method and print the result
    result = sol.countHillValley(nums_val)
    print(f"\nThe number of hills and valleys is: {result}")