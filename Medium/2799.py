from collections import Counter
from typing import List

class Solution:
  def countCompleteSubarrays(self, nums: List[int]) -> int:
    """
    Counts the number of complete subarrays in the given list `nums`.

    A subarray is complete if the number of distinct elements in it is equal
    to the number of distinct elements in the entire array `nums`.

    Args:
        nums: A list of integers.

    Returns:
        The number of complete subarrays.
    """
    ans = 0
    distinct = len(set(nums))
    count = Counter()
    l = 0
    for r, num in enumerate(nums):
      count[num] += 1
      while len(count) == distinct:
        count[nums[l]] -= 1
        if count[nums[l]] == 0:
          del count[nums[l]]
        l += 1
      # For the current right pointer `r`, all subarrays ending at `r` and
      # starting from any index from 0 up to `l - 1` (inclusive) are complete
      # because the window `nums[l:r+1]` is the smallest window ending at `r`
      # that contains all distinct elements.
      ans += l
    return ans

# Example Usage:
if __name__ == "__main__":
  sol = Solution()
  nums1 = [1, 3, 1, 2, 2]
  print(f"Number of complete subarrays for {nums1}: {sol.countCompleteSubarrays(nums1)}")

  nums2 = [5, 5, 5, 5, 5]
  print(f"Number of complete subarrays for {nums2}: {sol.countCompleteSubarrays(nums2)}")

  nums3 = [1, 2, 3, 4, 5]
  print(f"Number of complete subarrays for {nums3}: {sol.countCompleteSubarrays(nums3)}")

  nums4 = [1, 2, 1, 2, 3]
  print(f"Number of complete subarrays for {nums4}: {sol.countCompleteSubarrays(nums4)}")

  nums5 = []
  print(f"Number of complete subarrays for {nums5}: {sol.countCompleteSubarrays(nums5)}")