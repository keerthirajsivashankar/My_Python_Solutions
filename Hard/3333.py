import collections
import functools
import math
from typing import List

class Solution:
  def possibleStringCount(self, word: str, k: int) -> int:
    MOD = 1_000_000_007
    groups = self._getConsecutiveLetters(word)
    
    totalCombinations = functools.reduce(lambda subtotal, group:
                                         subtotal * group % MOD, groups)
    
    if k <= len(groups):
      return totalCombinations

    dp = [0] * k
    dp[0] = 1

    for i, group in enumerate(groups):
      newDp = [0] * k
      windowSum = 0
      for j in range(i, k):
        newDp[j] = (newDp[j] + windowSum) % MOD
        windowSum = (windowSum + dp[j]) % MOD
        if j >= group:
          windowSum = (windowSum - dp[j - group] + MOD) % MOD
      dp = newDp

    return (totalCombinations - sum(dp)) % MOD

  def _getConsecutiveLetters(self, word: str) -> List[int]:
    groups = []
    group = 1
    for i in range(1, len(word)):
      if word[i] == word[i - 1]:
        group += 1
      else:
        groups.append(group)
        group = 1
    groups.append(group)
    return groups

def get_string_input(prompt: str) -> str:
    return input(prompt)

def get_integer_input(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    sol = Solution()
    
    word_val = get_string_input("Enter the word: ")
    k_val = get_integer_input("Enter the integer k: ")

    result = sol.possibleStringCount(word_val, k_val)
    print(f"The possible string count is: {result}")