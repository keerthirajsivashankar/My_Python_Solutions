from collections import Counter
from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        """
        Counts the number of "good" subarrays in the given list `nums`.

        A subarray is "good" if the number of pairs (i, j) such that
        i < j and nums[i] == nums[j] is at least k.

        Args:
            nums: A list of integers.
            k: The minimum number of pairs required for a subarray to be "good".

        Returns:
            The total number of good subarrays.
        """
        cnt = Counter()
        ans = cur = 0
        i = 0
        for j, x in enumerate(nums):
            cur += cnt[x]
            cnt[x] += 1
            while cur - (cnt[nums[i]] - 1) >= k:
                cnt[nums[i]] -= 1
                cur -= (cnt[nums[i]])
                i += 1
            if cur >= k:
                ans += i + 1
        return ans

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 1, 1, 1, 1]
    k1 = 10
    print(f"Number of good subarrays for {nums1} with k={k1}: {sol.countGood(nums1, k1)}")

    nums2 = [1, 2, 3, 1, 2, 3]
    k2 = 2
    print(f"Number of good subarrays for {nums2} with k={k2}: {sol.countGood(nums2, k2)}")

    nums3 = [1, 1, 2, 2]
    k3 = 2
    print(f"Number of good subarrays for {nums3} with k={k3}: {sol.countGood(nums3, k3)}")

    nums4 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    k4 = 2
    print(f"Number of good subarrays for {nums4} with k={k4}: {sol.countGood(nums4, k4)}")

    nums5 = [1, 1, 1]
    k5 = 1
    print(f"Number of good subarrays for {nums5} with k={k5}: {sol.countGood(nums5, k5)}")

    nums6 = [1, 1, 1]
    k6 = 2
    print(f"Number of good subarrays for {nums6} with k={k6}: {sol.countGood(nums6, k6)}")