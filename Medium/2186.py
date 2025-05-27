class Solution:
  def differenceOfSums(self, n: int, m: int) -> int:
    summ = (1 + n) * n // 2
    num2 = self._getDivisibleSum(n, m)
    num1 = summ - num2
    return num1 - num2

  def _getDivisibleSum(self, n: int, m: int) -> int:
    last = n // m * m
    if last == 0:
      return 0
    first = m
    count = (last - first) // m + 1
    return (first + last) * count // 2

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
    m_val = get_integer_input("Enter the divisor (m): ")

    result = sol.differenceOfSums(n_val, m_val)
    print(f"The difference of sums is: {result}")