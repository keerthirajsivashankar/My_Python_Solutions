import itertools

class Solution:
  def possibleStringCount(self, word: str) -> int:
    return 1 + sum(a == b
                   for a, b in itertools.pairwise(word))

def get_string_input(prompt: str) -> str:
    return input(prompt)

if __name__ == "__main__":
    sol = Solution()
    
    word_val = get_string_input("Enter the word: ")

    result = sol.possibleStringCount(word_val)
    print(f"The possible string count is: {result}")