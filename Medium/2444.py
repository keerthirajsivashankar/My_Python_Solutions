from typing import List

class Solution:
  def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
    """
    Counts the number of subarrays in `nums` that contain both `minK` and `maxK`.

    Args:
        nums: A list of integers.
        minK: The minimum value that must be present in the subarray.
        maxK: The maximum value that must be present in the subarray.

    Returns:
        The number of subarrays containing both `minK` and `maxK`.
    """
    ans = 0
    j = -1  # Index of the element that violates the minK and maxK range
    prevMinKIndex = -1  # Index of the most recent occurrence of minK
    prevMaxKIndex = -1  # Index of the most recent occurrence of maxK

    for i, num in enumerate(nums):
      if num < minK or num > maxK:
        j = i  # Reset the valid subarray start
      if num == minK:
        prevMinKIndex = i
      if num == maxK:
        prevMaxKIndex = i

      # For the current ending index `i`, any starting index `k` in the range
      # [j + 1, min(prevMinKIndex, prevMaxKIndex)] will form a subarray
      # nums[k...i] that contains both minK and maxK.
      ans += max(0, min(prevMinKIndex, prevMaxKIndex) - j)

    return ans

# Example Usage:
if __name__ == "__main__":
  sol = Solution()
  nums1 = [1, 3, 5, 2, 7, 5]
  minK1 = 1
  maxK1 = 5
  print(f"Count for {nums1}, minK={minK1}, maxK={maxK1}: {sol.countSubarrays(nums1, minK1, maxK1)}")

  nums2 = [1, 1, 1, 1]
  minK2 = 1
  maxK2 = 1
  print(f"Count for {nums2}, minK={minK2}, maxK={maxK2}: {sol.countSubarrays(nums2, minK2, maxK2)}")

  nums3 = [1, 2, 3, 4, 5]
  minK3 = 2
  maxK3 = 4
  print(f"Count for {nums3}, minK={minK3}, maxK={maxK3}: {sol.countSubarrays(nums3, minK3, maxK3)}")

  nums4 = [2, 0, 2, 1, 2]
  minK4 = 1
  maxK4 = 2
  print(f"Count for {nums4}, minK={minK4}, maxK={maxK4}: {sol.countSubarrays(nums4, minK4, maxK4)}")

  nums5 = [3, 2, 1, 4, 5]
  minK5 = 1
  maxK5 = 3
  print(f"Count for {nums5}, minK={minK5}, maxK={maxK5}: {sol.countSubarrays(nums5, minK5, maxK5)}")