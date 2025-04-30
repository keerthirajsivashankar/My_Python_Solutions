from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """
        Counts the number of integers in the input list that have an even number of digits.

        Args:
            nums: A list of integers.

        Returns:
            The count of integers with an even number of digits.
        """
        count = 0
        for num in nums:
            num_str = str(num)
            if len(num_str) % 2 == 0:
                count += 1
        return count

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    nums1 = [12, 345, 2, 6, 7896]
    print(f"Number of even-digit numbers in {nums1}: {sol.findNumbers(nums1)}")

    nums2 = [555, 901, 482, 1771]
    print(f"Number of even-digit numbers in {nums2}: {sol.findNumbers(nums2)}")

    nums3 = [1]
    print(f"Number of even-digit numbers in {nums3}: {sol.findNumbers(nums3)}")

    nums4 = [10, 100, 1000]
    print(f"Number of even-digit numbers in {nums4}: {sol.findNumbers(nums4)}")