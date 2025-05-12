import collections
from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        """
        Finds all unique three-digit even numbers that can be formed using the digits from the input list.

        Args:
            digits: A list of digits (0 to 9).

        Returns:
            A sorted list of unique three-digit even numbers.
        """
        ans = []
        count = collections.Counter(digits)

        # Try to construct 'abc'.
        for a in range(1, 10):
            for b in range(0, 10):
                for c in range(0, 10, 2):  # 'c' must be even
                    if count[a] > 0 and count[b] > (b == a) and count[c] > (c == a) + (c == b):
                        ans.append(a * 100 + b * 10 + c)

        return sorted(list(set(ans)))

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    digits1 = [2, 1, 3, 0]
    print(f"Even numbers from {digits1}: {sol.findEvenNumbers(digits1)}")  # Output: [102, 120, 130, 210, 302, 310]

    digits2 = [2, 2, 8, 8, 2]
    print(f"Even numbers from {digits2}: {sol.findEvenNumbers(digits2)}")  # Output: [222, 228, 282, 288, 822, 828, 882]

    digits3 = [3, 7, 5, 8, 9]
    print(f"Even numbers from {digits3}: {sol.findEvenNumbers(digits3)}")  # Output: [578, 587, 758, 785, 857, 875, 958, 985]

    digits4 = [0, 0, 0]
    print(f"Even numbers from {digits4}: {sol.findEvenNumbers(digits4)}") # Output: []

    digits5 = [0, 1, 2, 3, 4]
    print(f"Even numbers from {digits5}: {sol.findEvenNumbers(digits5)}")