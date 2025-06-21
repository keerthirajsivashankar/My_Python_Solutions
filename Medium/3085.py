import math
import collections

class Solution:
  def minimumDeletions(self, word: str, k: int) -> int:
    ans = math.inf
    count = collections.Counter(word)

    for minFreq in count.values():
      deletions = 0
      for freq in count.values():
        if freq < minFreq:
          deletions += freq
        else:
          deletions += max(0, freq - (minFreq + k))
      ans = min(ans, deletions)

    return ans

def get_string_input(prompt: str) -> str:
    while True:
        s_val = input(prompt)
        if s_val.isalpha():
            return s_val
        else:
            print("Invalid input. Please enter a string containing only alphabetic characters.")

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
    
    word_val = get_string_input("Enter the word (e.g., 'aabbcc'): ")
    k_val = get_integer_input("Enter the integer k: ")

    result = sol.minimizeMax(word_val, k_val)
    print(f"The minimum number of deletions is: {result}")