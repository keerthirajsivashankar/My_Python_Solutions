from typing import List

class Solution:
  def countSubarrays(self, nums: List[int]) -> int:
    """
    Counts the number of arithmetic subarrays of length 3 in the given list.

    An arithmetic subarray of length 3 is a contiguous subarray [a, b, c]
    where b - a == c - b, which is equivalent to b == (a + c) / 2
    or b * 2 == a + c.

    Args:
        nums: A list of integers.

    Returns:
        The number of arithmetic subarrays of length 3.
    """
    count = 0
    for i in range(len(nums) - 2):
      a = nums[i]
      b = nums[i + 1]
      c = nums[i + 2]
      if b * 2 == a + c:
        count += 1
    return count

# Example Usage:
if __name__ == "__main__":
  sol = Solution()
  nums1 = [1, 2, 3, 4]
  print(f"Count of arithmetic subarrays: {sol.countSubarrays(nums1)}")

  nums2 = [1, 1, 1, 1]
  print(f"Count of arithmetic subarrays: {sol.countSubarrays(nums2)}")

  nums3 = [1, 3, 5, 7]
  print(f"Count of arithmetic subarrays: {sol.countSubarrays(nums3)}")

  nums4 = [2, 4, 1, 3]
  print(f"Count of arithmetic subarrays: {sol.countSubarrays(nums4)}")

  nums5 = [0, 0, 0]
  print(f"Count of arithmetic subarrays: {sol.countSubarrays(nums5)}")

  nums6 = [1, 2, 4, 8]
  print(f"Count of arithmetic subarrays: {sol.countSubarrays(nums6)}")