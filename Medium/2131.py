from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0
        center_used = False

        for word in count:
            rev = word[::-1]
            if word[0] == word[1]:
                pairs = count[word] // 2
                length += pairs * 4
                if count[word] % 2 == 1 and not center_used:
                    length += 2
                    center_used = True
            elif word < rev:
                pairs = min(count[word], count[rev])
                length += pairs * 4

        return length

def get_words_input() -> List[str]:
    while True:
        try:
            input_str = input("Enter words separated by spaces (e.g., 'lc cl gg gg'): ")
            words = [s.strip() for s in input_str.split()]
            # Optional: Basic validation for 2-character words if problem constrains it
            if not all(len(word) == 2 for word in words):
                print("Please ensure all words have exactly two characters.")
                continue
            return words
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    sol = Solution()
    
    print("This program finds the length of the longest palindrome that can be built from a list of two-character words.")
    words = get_words_input()
    
    if words:
        result = sol.longestPalindrome(words)
        print(f"The longest palindrome length is: {result}")
    else:
        print("No words were entered. Cannot form a palindrome.")