import math
import collections

class Solution:
  def maxDifference(self, s: str, k: int) -> int:
    ans = -math.inf
    permutations = [(a, b) for a in '01234' for b in '01234' if a != b]

    for a, b in permutations:
      minDiff = collections.defaultdict(lambda: math.inf)
      prefixA = [0]
      prefixB = [0]

      l = 0
      for r, c in enumerate(s):
        prefixA.append(prefixA[-1] + int(c == a))
        prefixB.append(prefixB[-1] + int(c == b))
        while (r - l + 1 >= k and
               prefixA[l] < prefixA[-1] and
               prefixB[l] < prefixB[-1]):
          paritiesKey = (prefixA[l] % 2, prefixB[l] % 2)
          minDiff[paritiesKey] = min(minDiff[paritiesKey],
                                     prefixA[l] - prefixB[l])
          l += 1
        
        if (1 - prefixA[-1] % 2, prefixB[-1] % 2) in minDiff:
            ans = max(ans, (prefixA[-1] - prefixB[-1]) -
                      minDiff[(1 - prefixA[-1] % 2, prefixB[-1] % 2)])
        else:
            pass


    return ans

def get_string_input(prompt: str) -> str:
    while True:
        s_val = input(prompt)
        if all(char in '01234' for char in s_val):
            return s_val
        else:
            print("String must contain only digits '0', '1', '2', '3', '4'.")

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
    
    s_val = get_string_input("Enter the string s (digits '0'-'4' only): ")
    k_val = get_integer_input("Enter the integer k (window size): ")

    result = sol.maxDifference(s_val, k_val)
    print(f"The maximum difference is: {result}")