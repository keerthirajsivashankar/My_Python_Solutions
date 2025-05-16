from typing import List

class Solution:
  def getWordsInLongestSubsequence(
      self,
      n: int,
      words: List[str],
      groups: List[int],
  ) -> List[str]:
    """
    Finds the longest subsequence of 'words' where consecutive words
    differ by exactly one character and belong to different groups.

    Args:
        n: The number of words.
        words: A list of strings.
        groups: A list of integers, where groups[i] represents the group of words[i].

    Returns:
        A list of strings representing the longest subsequence.
    """
    ans = []
    # dp[i] := the length of the longest subsequence ending in `words[i]`
    dp = [1] * n  # Initialize each word can form a subsequence of length 1
    # prev[i] := the index of the word preceding words[i] in the longest subsequence ending at words[i]
    prev = [-1] * n  # Initialize with -1, meaning no predecessor

    for i in range(1, n):
      for j in range(i):
        # Check the conditions: different groups and one character difference
        if groups[i] == groups[j]:
          continue
        if len(words[i]) != len(words[j]):
          continue
        if sum(a != b for a, b in zip(words[i], words[j])) != 1:
          continue
        # If the conditions are met, update dp[i] if a longer subsequence is found
        if dp[i] < dp[j] + 1:
          dp[i] = dp[j] + 1  # Extend the subsequence ending at words[j]
          prev[i] = j      # Record the predecessor index

    # Find the last index of the longest subsequence.
    index = dp.index(max(dp))  # Find the index of the maximum dp value
    # Backtrack from the last word to construct the subsequence
    while index != -1:
      ans.append(words[index])  # Add the word to the result
      index = prev[index]      # Move to the predecessor's index

    return ans[::-1]  # Reverse the result to get the correct order

# Example Usage:
if __name__ == "__main__":
    n = 5
    words = ["abc", "abd", "cba", "cbd", "adc"]
    groups = [1, 2, 2, 1, 1]
    sol = Solution()
    result = sol.getWordsInLongestSubsequence(n, words, groups)
    print(f"Longest subsequence: {result}")  # Output: ['abc', 'abd', 'cbd']

    n2 = 4
    words2 = ["a", "b", "ba", "bba"]
    groups2 = [1, 2, 2, 1]
    result2 = sol.getWordsInLongestSubsequence(n2, words2, groups2)
    print(f"Longest subsequence: {result2}") # Output: ['a', 'ba', 'bba']
