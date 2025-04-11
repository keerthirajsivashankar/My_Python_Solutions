class Solution:
  def countSymmetricIntegers(self, low: int, high: int) -> int:
    def isSymmetricInteger(num: int) -> bool:
      s = str(num)
      n = len(s)
      if n % 2 != 0:
        return False
      mid = n // 2
      left_sum = 0
      right_sum = 0
      for i in range(mid):
        left_sum += int(s[i])
      for i in range(mid, n):
        right_sum += int(s[i])
      return left_sum == right_sum

    count = 0
    for num in range(low, high + 1):
      if isSymmetricInteger(num):
        count += 1
    return count

# Example Usage:
if __name__ == "__main__":
  sol = Solution()
  low1 = 1
  high1 = 100
  print(f"Count of symmetric integers between {low1} and {high1}: {sol.countSymmetricIntegers(low1, high1)}")

  low2 = 1000
  high2 = 9999
  print(f"Count of symmetric integers between {low2} and {high2}: {sol.countSymmetricIntegers(low2, high2)}")

  low3 = 1
  high3 = 1
  print(f"Count of symmetric integers between {low3} and {high3}: {sol.countSymmetricIntegers(low3, high3)}")

  low4 = 10
  high4 = 11
  print(f"Count of symmetric integers between {low4} and {high4}: {sol.countSymmetricIntegers(low4, high4)}")

  low5 = 99
  high5 = 100
  print(f"Count of symmetric integers between {low5} and {high5}: {sol.countSymmetricIntegers(low5, high5)}")

  low6 = 1234
  high6 = 4321
  print(f"Count of symmetric integers between {low6} and {high6}: {sol.countSymmetricIntegers(low6, high6)}")