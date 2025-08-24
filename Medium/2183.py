from typing import List

class Solution:
  def longestSubarray(self, nums: List[int]) -> int:
    """
    Finds the length of the longest subarray containing at most one zero.
    
    This is solved using a sliding window approach.
    
    Args:
      nums: A list of integers (0s and 1s).
      
    Returns:
      The length of the longest subarray with at most one zero.
    """
    left = 0
    zero_count = 0
    max_len = 0
    
    # The 'right' pointer iterates through the array, expanding the window.
    for right in range(len(nums)):
      # If the current element is a zero, increment our zero counter.
      if nums[right] == 0:
        zero_count += 1
      
      # While the window contains more than one zero, we need to shrink it.
      while zero_count > 1:
        # If the element at the 'left' pointer is a zero, decrement the count.
        if nums[left] == 0:
          zero_count -= 1
        # Move the 'left' pointer forward, effectively shrinking the window.
        left += 1
      
      # The length of the current valid window is 'right - left'.
      # We update max_len with the largest valid length found so far.
      max_len = max(max_len, right - left)
    
    # The problem asks for the longest subarray *after deleting one element*.
    # If the original array contains only 1s, the length will be 'right - left'
    # which is `len(nums) - 1` (the correct answer). If there are zeros, the
    # `right - left` value is already the length of the longest subarray
    # of ones after removing one zero.
    
    return max_len

# --- Example Usage ---
if __name__ == "__main__":
    solution = Solution()

    # Example 1: `nums` with zeros
    nums1 = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    result1 = solution.longestSubarray(nums1)
    print(f"For nums = {nums1}, the longest subarray length is: {result1}") # Expected: 5 (from [1, 1, 1, 0, 1])

    # Example 2: `nums` with only ones
    nums2 = [1, 1, 1, 1, 1]
    result2 = solution.longestSubarray(nums2)
    print(f"For nums = {nums2}, the longest subarray length is: {result2}") # Expected: 4 (after removing one element)

    # Example 3: `nums` with only one zero
    nums3 = [1, 1, 0, 1, 1, 1]
    result3 = solution.longestSubarray(nums3)
    print(f"For nums = {nums3}, the longest subarray length is: {result3}") # Expected: 5
