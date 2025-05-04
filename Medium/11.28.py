import collections
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """
        Finds the number of equivalent domino pairs in a list of dominoes.

        Two dominoes are equivalent if they have the same numbers on their faces,
        regardless of their orientation. For example, [1, 2] and [2, 1] are equivalent.

        Args:
            dominoes: A list of dominoes, where each domino is represented by a list of two integers.

        Returns:
            The number of equivalent domino pairs.
        """
        ans = 0
        count = collections.Counter()

        for domino in dominoes:
            # Create a unique key for each equivalent domino pair
            # by taking the smaller number as the tens digit and the larger
            # number as the units digit. This ensures that [1, 2] and [2, 1]
            # will have the same key (12).
            key = min(domino[0], domino[1]) * 10 + max(domino[0], domino[1])
            ans += count[key]  # Add the count of previously seen equivalent dominoes
            count[key] += 1    # Increment the count for the current domino's equivalent type

        return ans

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    dominoes1 = [[1, 2], [2, 1], [3, 4], [5, 6]]
    print(f"Number of equivalent pairs in {dominoes1}: {sol.numEquivDominoPairs(dominoes1)}")

    dominoes2 = [[1, 2], [1, 2], [1, 2], [1, 2], [2, 1], [2, 1]]
    print(f"Number of equivalent pairs in {dominoes2}: {sol.numEquivDominoPairs(dominoes2)}")

    dominoes3 = [[1, 1], [1, 1], [1, 1]]
    print(f"Number of equivalent pairs in {dominoes3}: {sol.numEquivDominoPairs(dominoes3)}")

    dominoes4 = [[1, 2]]
    print(f"Number of equivalent pairs in {dominoes4}: {sol.numEquivDominoPairs(dominoes4)}")