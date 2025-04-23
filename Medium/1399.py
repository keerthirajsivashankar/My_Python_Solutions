class Solution:
  def countLargestGroup(self, n: int) -> int:
    """
    Counts the number of groups with the largest size formed by numbers from 1 to n,
    where each group contains numbers having the same digit sum.

    Args:
        n: An integer representing the upper limit of the numbers (inclusive).

    Returns:
        The number of groups with the largest size.
    """
    count = [0] * (9 * 4 + 1)  # Maximum possible digit sum for n <= 10^4 is 9+9+9+9 = 36
    for i in range(1, n + 1):
      count[self._getDigitSum(i)] += 1

    max_size = 0
    for c in count:
      max_size = max(max_size, c)

    largest_group_count = 0
    for c in count:
      if c == max_size:
        largest_group_count += 1

    return largest_group_count

  def _getDigitSum(self, num: int) -> int:
    """
    Calculates the digit sum of a given integer.

    Args:
        num: An integer.

    Returns:
        The sum of the digits of the integer.
    """
    return sum(int(digit) for digit in str(num))

# Example Usage:
if __name__ == "__main__":
  sol = Solution()
  n1 = 13
  print(f"Number of largest groups for n={n1}: {sol.countLargestGroup(n1)}")

  n2 = 5
  print(f"Number of largest groups for n={n2}: {sol.countLargestGroup(n2)}")

  n3 = 100
  print(f"Number of largest groups for n={n3}: {sol.countLargestGroup(n3)}")

  n4 = 9999
  print(f"Number of largest groups for n={n4}: {sol.countLargestGroup(n4)}")