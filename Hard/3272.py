import collections
import math

class Solution:
  def countGoodIntegers(self, n: int, k: int) -> int:
    halfLength = (n + 1) // 2
    minHalf = 10**(halfLength - 1)
    maxHalf = 10**halfLength
    ans = 0
    seen = set()

    for num in range(minHalf, maxHalf):
      palindrome = str(num) + str(num)[::-1][n % 2:]
      sortedDigits = ''.join(sorted(palindrome))
      if int(palindrome) % k != 0 or sortedDigits in seen:
        continue
      seen.add(sortedDigits)
      digitCount = collections.Counter(palindrome)
      # Leading zeros are not allowed, so the first digit is special.
      firstDigitChoices = n - digitCount['0']
      if firstDigitChoices <= 0 and '0' in digitCount and n > 1:
          continue # Skip if all digits are zero and n > 1

      permutations = firstDigitChoices * math.factorial(n - 1) if n > 0 and firstDigitChoices > 0 else 0

      # For each repeated digit, divide by the factorial of the frequency since
      # permutations that swap identical digits don't create a new number.
      for freq in digitCount.values():
        if freq > 1:
          permutations //= math.factorial(freq)
      ans += permutations

    return ans

if __name__ == "__main__":
  solution = Solution()
  while True:
    try:
      n_input = int(input("Enter the desired length of the integer (n): "))
      if n_input <= 0:
        print("Please enter a positive integer for the length.")
        continue
      k_input = int(input("Enter the divisor (k): "))
      result = solution.countGoodIntegers(n_input, k_input)
      print(f"The number of good integers of length {n_input} divisible by {k_input} is: {result}")
      break # Exit the loop after successful input and calculation
    except ValueError:
      print("Invalid input. Please enter integers only.")
    except KeyboardInterrupt:
      print("\nExiting the program.")
      break