class Solution:
  def countGoodNumbers(self, n: int) -> int:
    MOD = 1_000_000_007

    def modPow(x: int, n: int) -> int:
      if n == 0:
        return 1
      if n % 2 == 1:
        return (x * modPow(x, n - 1)) % MOD
      return modPow((x * x) % MOD, n // 2)

    return (modPow(20, n // 2) * (1 if n % 2 == 0 else 5)) % MOD

if __name__ == "__main__":
  solution = Solution()
  while True:
    try:
      n_input = int(input("Enter the desired length of the good number (n): "))
      if n_input < 0:
        print("Please enter a non-negative integer for the length.")
        continue
      result = solution.countGoodNumbers(n_input)
      print(f"The number of good numbers of length {n_input} is: {result}")
      break  # Exit the loop after successful input and calculation
    except ValueError:
      print("Invalid input. Please enter an integer only.")
    except KeyboardInterrupt:
      print("\nExiting the program.")
      break