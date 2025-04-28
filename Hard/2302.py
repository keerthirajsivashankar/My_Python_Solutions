from typing import List

class Solution:
  def countSubarrays(self, nums: List[int], k: int) -> int:
    """
    Counts the number of contiguous subarrays in `nums` whose product is strictly less than `k`.

    Args:
        nums: A list of integers.
        k: The upper bound for the product of the subarrays.

    Returns:
        The number of contiguous subarrays with a product less than `k`.
    """
    ans = 0
    product = 1
    left = 0
    for right, num in enumerate(nums):
      product *= num
      while product >= k and left <= right:
        product //= nums[left]
        left += 1
      ans += right - left + 1
    return ans

# Example Usage:
if __name__ == "__main__":
  sol = Solution()
  nums1 = [1, 10, 3, 4, 2]
  k1 = 100
  print(f"Count of subarrays with product < {k1}: {sol.countSubarrays(nums1, k1)}")

  nums2 = [1, 2, 3]
  k2 = 0
  print(f"Count of subarrays with product < {k2}: {sol.countSubarrays(nums2, k2)}")

  nums3 = [8, 2, 6, 5]
  k3 = 50
  print(f"Count of subarrays with product < {k3}: {sol.countSubarrays(nums3, k3)}")

  nums4 = [1, 1, 1]
  k4 = 1
  print(f"Count of subarrays with product < {k4}: {sol.countSubarrays(nums4, k4)}")