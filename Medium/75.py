from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Counts the number of fair pairs (i, j) such that i < j and lower <= nums[i] + nums[j] <= upper.

        Args:
            nums: A list of integers.
            lower: The lower bound for the sum of a fair pair.
            upper: The upper bound for the sum of a fair pair.

        Returns:
            The number of fair pairs.
        """
        nums.sort()

        def countLessOrEqual(summ: int) -> int:
            res = 0
            left = 0
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] <= summ:
                    res += right - left
                    left += 1
                else:
                    right -= 1
            return res

        return countLessOrEqual(upper) - countLessOrEqual(lower - 1)

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    nums1 = [0, 1, 7, 4, 4, 5]
    lower1 = 3
    upper1 = 6
    print(f"Fair pairs for {nums1} in range [{lower1}, {upper1}]: {sol.countFairPairs(nums1, lower1, upper1)}")

    nums2 = [1, 2, 3, 4, 5]
    lower2 = 1
    upper2 = 10
    print(f"Fair pairs for {nums2} in range [{lower2}, {upper2}]: {sol.countFairPairs(nums2, lower2, upper2)}")

    nums3 = [1, 2, 3, 4, 5]
    lower3 = 3
    upper3 = 7
    print(f"Fair pairs for {nums3} in range [{lower3}, {upper3}]: {sol.countFairPairs(nums3, lower3, upper3)}")

    nums4 = [1, 1, 1, 1, 1]
    lower4 = 2
    upper4 = 2
    print(f"Fair pairs for {nums4} in range [{lower4}, {upper4}]: {sol.countFairPairs(nums4, lower4, upper4)}")

    nums5 = [-1, 0, 1, 2]
    lower5 = -1
    upper5 = 1
    print(f"Fair pairs for {nums5} in range [{lower5}, {upper5}]: {sol.countFairPairs(nums5, lower5, upper5)}")