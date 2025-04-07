class Solution:
  def canPartition(self, nums: list[int]) -> bool:
    """
    Determines if a list of numbers can be partitioned into two subsets with equal sum.

    Args:
        nums: A list of integers.

    Returns:
        True if the list can be partitioned, False otherwise.
    """
    summ = sum(nums)
    if summ % 2 == 1:
      return False
    return self.knapsack_(nums, summ // 2)

  def knapsack_(self, nums: list[int], subsetSum: int) -> bool:
    """
    Helper function to determine if a subset with a given sum exists.

    Args:
        nums: A list of integers.
        subsetSum: The target subset sum.

    Returns:
        True if a subset with the given sum exists, False otherwise.
    """
    # dp[i] := True if i can be formed by nums so far
    dp = [False] * (subsetSum + 1)
    dp[0] = True

    for num in nums:
      for i in range(subsetSum, num - 1, -1):
        dp[i] = dp[i] or dp[i - num]

    return dp[subsetSum]

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 5, 11, 5]
    result1 = sol.canPartition(nums1)
    print(f"Can {nums1} be partitioned? {result1}")

    nums2 = [1, 2, 3, 5]
    result2 = sol.canPartition(nums2)
    print(f"Can {nums2} be partitioned? {result2}")

    nums3 = [2, 2, 3, 5]
    result3 = sol.canPartition(nums3)
    print(f"Can {nums3} be partitioned? {result3}")

    nums4 = [10, 4, 6, 3, 7, 9, 2]
    result4 = sol.canPartition(nums4)
    print(f"Can {nums4} be partitioned? {result4}")

    nums5 = [1, 1, 1, 1, 1]
    result5 = sol.canPartition(nums5)
    print(f"Can {nums5} be partitioned? {result5}")

    nums6 = [1]
    result6 = sol.canPartition(nums6)
    print(f"Can {nums6} be partitioned? {result6}")

    nums7 = []
    result7 = sol.canPartition(nums7)
    print(f"Can {nums7} be partitioned? {result7}")