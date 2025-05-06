from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans: List[List[int]] = []

        def nSum(
            l: int, r: int, target: int, n: int, path: List[int],
            ans: List[List[int]]) -> None:
            """Finds n numbers that add up to the target in [l, r]."""
            if r - l + 1 < n or n < 2 or target < nums[l] * n or target > nums[r] * n:
                return
            if n == 2:
                while l < r:
                    summ = nums[l] + nums[r]
                    if summ == target:
                        ans.append(path + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif summ < target:
                        l += 1
                    else:
                        r -= 1
                return

            for i in range(l, r + 1):
                if i > l and nums[i] == nums[i - 1]:
                    continue

                nSum(i + 1, r, target - nums[i], n - 1, path + [nums[i]], ans)

        nums.sort()
        nSum(0, len(nums) - 1, target, 4, [], ans)
        return ans

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    print(f"Four sum for {nums1} with target {target1}: {sol.fourSum(nums1, target1)}")

    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    print(f"Four sum for {nums2} with target {target2}: {sol.fourSum(nums2, target2)}")

    nums3 = [-2, -1, 0, 0, 1, 2]
    target3 = 0
    print(f"Four sum for {nums3} with target {target3}: {sol.fourSum(nums3, target3)}")