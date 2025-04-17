import collections
import math

class Solution:
  def countPairs(self, nums: list[int], k: int) -> int:
    ans = 0
    numToIndices = collections.defaultdict(list)

    for i, num in enumerate(nums):
      numToIndices[num].append(i)

    for indices in numToIndices.values():
      gcds = collections.Counter()
      for i in indices:
        gcd_i = math.gcd(i, k)
        for gcd_j, count in gcds.items():
          if (gcd_i * gcd_j) % k == 0:
            ans += count
        gcds[gcd_i] += 1

    return ans

# Example Usage:
if __name__ == "__main__":
  sol = Solution()
  nums1 = [3, 0, 1, 5, 2]
  k1 = 3
  print(f"Number of pairs for {nums1} with k={k1}: {sol.countPairs(nums1, k1)}")

  nums2 = [1, 2, 3, 4, 5]
  k2 = 1
  print(f"Number of pairs for {nums2} with k={k2}: {sol.countPairs(nums2, k2)}")

  nums3 = [1, 2, 3, 4, 5]
  k3 = 2
  print(f"Number of pairs for {nums3} with k={k3}: {sol.countPairs(nums3, k3)}")

  nums4 = [1, 2, 3, 4, 5]
  k4 = 5
  print(f"Number of pairs for {nums4} with k={k4}: {sol.countPairs(nums4, k4)}")

  nums5 = [1, 2, 1, 2]
  k5 = 2
  print(f"Number of pairs for {nums5} with k={k5}: {sol.countPairs(nums5, k5)}")

  nums6 = [0, 0, 0, 0]
  k6 = 5
  print(f"Number of pairs for {nums6} with k={k6}: {sol.countPairs(nums6, k6)}")