from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]

if __name__ == "__main__":
    sol = Solution()

    words1 = ["abc", "bcd", "abca", "cde"]
    x1 = "a"
    print(f"Words: {words1}, Character: '{x1}' -> Indices: {sol.findWordsContaining(words1, x1)}")

    words2 = ["apple", "banana", "cherry"]
    x2 = "e"
    print(f"Words: {words2}, Character: '{x2}' -> Indices: {sol.findWordsContaining(words2, x2)}")

    words3 = ["hello", "world"]
    x3 = "z"
    print(f"Words: {words3}, Character: '{x3}' -> Indices: {sol.findWordsContaining(words3, x3)}")

    words4 = ["", "abc", "def"]
    x4 = "a"
    print(f"Words: {words4}, Character: '{x4}' -> Indices: {sol.findWordsContaining(words4, x4)}")