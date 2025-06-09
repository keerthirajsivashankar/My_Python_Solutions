class Solution:
  def findKthNumber(self, n: int, k: int) -> int:
    ans = 1

    i = 1
    while i < k:
      gap = self._getGap(ans, ans + 1, n)
      if i + gap <= k:
        i += gap
        ans += 1
      else:
        i += 1
        ans *= 10

    return ans

  def _getGap(self, a: int, b: int, n: int) -> int:
    gap = 0
    while a <= n:
      gap += min(n + 1, b) - a
      a *= 10
      b *= 10
    return gap

def get_integer_input(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    sol = Solution()
    
    n_val = get_integer_input("Enter the upper limit (n): ")
    k_val = get_integer_input("Enter the value of k (kth number): ")

    result = sol.findKthNumber(n_val, k_val)
    print(f"The {k_val}-th lexicographical number up to {n_val} is: {result}")