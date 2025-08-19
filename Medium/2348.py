from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        Calculates the number of zero-filled subarrays in an array of integers.

        This solution uses a single pass and a clever way to count subarrays
        by tracking the index of the last non-zero element.

        Args:
          nums: A list of integers.

        Returns:
          The total number of zero-filled subarrays.
        """
        ans = 0
        # Initialize index to -1 to correctly handle subarrays starting at index 0.
        index = -1

        # Iterate through the array with both the index and the number.
        for i, num in enumerate(nums):
            # If the current number is non-zero (truthy), update the index.
            if num:
                index = i
            # If the current number is a zero, it means we're in a zero-filled subarray.
            else:
                # The length of the current contiguous zero subarray ending at i
                # is simply the difference between the current index and the index
                # of the last non-zero number. Add this length to the total count.
                ans += i - index

        return ans

# --- Example Usage ---
def get_list_of_integers_input(prompt: str) -> List[int]:
    """Helper function to get a list of integers from the user."""
    while True:
        try:
            input_str = input(prompt)
            elements = [int(x) for x in input_str.split()]
            return elements
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    sol = Solution()
    
    print("--- Zero-Filled Subarray Counter ---")
    
    # Get the array of numbers from the user
    nums_val = get_list_of_integers_input("Enter numbers for the array separated by spaces (e.g., '1 0 0 2 0 0 0 1'): ")

    # Call the solution method and print the result
    result = sol.zeroFilledSubarray(nums_val)
    print(f"\nFor the array {nums_val}, the number of zero-filled subarrays is: {result}")
