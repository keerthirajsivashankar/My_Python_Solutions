from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        """
        Calculates the number of valid arrays that can be formed from the given differences
        and the specified lower and upper bounds for the first element.

        Args:
            differences: A list of integers representing the differences between consecutive elements
                         of the original array.
            lower: The lower bound for the first element of the original array.
            upper: The upper bound for the first element of the original array.

        Returns:
            The number of valid original arrays.
        """
        curr = 0
        min_val = 0
        max_val = 0

        for num in differences:
            curr += num
            min_val = min(curr, min_val)
            max_val = max(curr, max_val)

        min_start = lower - min_val
        max_start = upper - max_val

        return max(0, max_start - min_start + 1)

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    differences1 = [1, -3, 4]
    lower1 = 1
    upper1 = 6
    print(f"Number of arrays for differences {differences1}, lower {lower1}, upper {upper1}: {sol.numberOfArrays(differences1, lower1, upper1)}")

    differences2 = [3, -4, 5, 1, -2]
    lower2 = -4
    upper2 = 5
    print(f"Number of arrays for differences {differences2}, lower {lower2}, upper {upper2}: {sol.numberOfArrays(differences2, lower2, upper2)}")

    differences3 = [0]
    lower3 = -10
    upper3 = 10
    print(f"Number of arrays for differences {differences3}, lower {lower3}, upper {upper3}: {sol.numberOfArrays(differences3, lower3, upper3)}")

    differences4 = []
    lower4 = 5
    upper4 = 8
    print(f"Number of arrays for differences {differences4}, lower {lower4}, upper {upper4}: {sol.numberOfArrays(differences4, lower4, upper4)}")