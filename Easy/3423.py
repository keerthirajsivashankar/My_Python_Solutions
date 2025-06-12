from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        m = abs(nums[0] - nums[-1])

        for i in range(n - 1):
            m = max(m, abs(nums[i] - nums[i + 1]))

        return m

if __name__ == "_main_":
    nums = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
    sol = Solution()
    result = sol.maxAdjacentDistance(nums)
    print("Maximum adjacent distance:", result)