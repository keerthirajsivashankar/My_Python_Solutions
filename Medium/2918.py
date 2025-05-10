from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Finds the minimum possible sum of two arrays after replacing all zeros with some positive integers
        such that the sums of both arrays become equal.

        Args:
            nums1: The first list of integers.
            nums2: The second list of integers.

        Returns:
            The minimum equal sum if possible, otherwise -1.
        """
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        zero1 = nums1.count(0)
        zero2 = nums2.count(0)

        # If nums1 has no zeros and its current sum is less than the minimum possible sum of nums2, it's impossible.
        if zero1 == 0 and sum1 < sum2 + zero2:
            return -1

        # If nums2 has no zeros and its current sum is less than the minimum possible sum of nums1, it's impossible.
        if zero2 == 0 and sum2 < sum1 + zero1:
            return -1

        # If both have zeros, we want to increase the smaller sum to meet the larger sum.
        # If sums are initially equal, we don't need to add anything to the zeros (effectively replacing with 1 if there are zeros).
        # The minimum equal sum will be the maximum of the minimum possible sums of both arrays.
        return max(sum1 + zero1, sum2 + zero2)

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    nums1_1 = [1, 2, 0]
    nums2_1 = [3]
    print(f"Minimum sum for {nums1_1}, {nums2_1}: {sol.minSum(nums1_1, nums2_1)}")

    nums1_2 = [1, 2, 3]
    nums2_2 = [4, 5, 6]
    print(f"Minimum sum for {nums1_2}, {nums2_2}: {sol.minSum(nums1_2, nums2_2)}")

    nums1_3 = [0, 0]
    nums2_3 = [0, 0]
    print(f"Minimum sum for {nums1_3}, {nums2_3}: {sol.minSum(nums1_3, nums2_3)}")

    nums1_4 = [0, 0]
    nums2_4 = [1, 2]
    print(f"Minimum sum for {nums1_4}, {nums2_4}: {sol.minSum(nums1_4, nums2_4)}")

    nums1_5 = [1, 2]
    nums2_5 = [0, 0]
    print(f"Minimum sum for {nums1_5}, {nums2_5}: {sol.minSum(nums1_5, nums2_5)}")

    nums1_6 = [2, 0, 2]
    nums2_6 = [1, 4]
    print(f"Minimum sum for {nums1_6}, {nums2_6}: {sol.minSum(nums1_6, nums2_6)}")