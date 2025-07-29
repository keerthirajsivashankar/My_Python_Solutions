from typing import List

class Solution:
  def smallestSubarrays(self, nums: List[int]) -> List[int]:
    MAX_BIT = 30
    ans = [1] * len(nums)
    # closest[j] stores the index of the rightmost occurrence of the j-th bit being 1
    closest = [0] * MAX_BIT

    # Iterate through the array from right to left
    for i in reversed(range(len(nums))):
      # For each bit position from 0 to MAX_BIT-1
      for j in range(MAX_BIT):
        # If the j-th bit of nums[i] is set (i.e., is 1)
        if nums[i] >> j & 1:
          # Update closest[j] to the current index 'i'
          closest[j] = i
        # The length of the smallest subarray starting at 'i'
        # that includes all bits set in the suffix nums[i...]
        # is determined by the furthest 'closest' bit encountered so far.
        # We want the subarray to extend at least to the rightmost occurrence
        # of any bit that is already present in nums[i] or any bit that appears
        # to the right of 'i'.
        # max(ans[i], closest[j] - i + 1) updates ans[i] to be the maximum
        # length required to cover all '1' bits that are relevant for the suffix starting at 'i'.
        ans[i] = max(ans[i], closest[j] - i + 1)

    return ans

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

if __name__ == "__main__":
    sol = Solution()
    
    print("--- Smallest Subarrays with Maximum OR ---")
    
    nums_val = get_list_of_integers_input("Enter numbers for the array separated by spaces (e.g., '1 0 2 1 3'): ")

    result = sol.smallestSubarrays(nums_val)
    print(f"\nLengths of smallest subarrays with maximum OR sum: {result}")