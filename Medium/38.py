class Solution:
  def countAndSay(self, n: int) -> str:
    """
    Generates the nth term of the count-and-say sequence.

    Args:
        n: The index of the term to generate (1-based).

    Returns:
        The nth term of the count-and-say sequence as a string.
    """
    if n <= 0:
      return ""
    ans = '1'

    for _ in range(n - 1):
      nxt = ''
      i = 0
      while i < len(ans):
        count = 1
        while i + 1 < len(ans) and ans[i] == ans[i + 1]:
          count += 1
          i += 1
        nxt += str(count) + ans[i]
        i += 1
      ans = nxt

    return ans

# Example Usage:
if __name__ == "__main__":
  sol = Solution()
  print(f"Count and Say (1): {sol.countAndSay(1)}")
  print(f"Count and Say (2): {sol.countAndSay(2)}")
  print(f"Count and Say (3): {sol.countAndSay(3)}")
  print(f"Count and Say (4): {sol.countAndSay(4)}")
  print(f"Count and Say (5): {sol.countAndSay(5)}")
  print(f"Count and Say (0): {sol.countAndSay(0)}")