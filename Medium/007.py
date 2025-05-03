from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        Finds the minimum number of rotations to make all values in either
        'tops' or 'bottoms' equal to the same number.

        Args:
            tops: A list of integers representing the top values of dominoes.
            bottoms: A list of integers representing the bottom values of dominoes.

        Returns:
            The minimum number of rotations needed, or -1 if it's impossible.
        """

        def check(target: int, top_row: List[int], bottom_row: List[int]) -> int:
            """
            Checks if it's possible to make either row all 'target' and returns
            the minimum rotations needed for that row. Returns -1 if impossible.
            """
            rotations_top = 0
            rotations_bottom = 0
            possible_top = True
            possible_bottom = True

            for i in range(len(top_row)):
                if top_row[i] != target and bottom_row[i] != target:
                    possible_top = False
                elif top_row[i] != target:
                    rotations_top += 1

                if bottom_row[i] != target and top_row[i] != target:
                    possible_bottom = False
                elif bottom_row[i] != target:
                    rotations_bottom += 1

            if possible_top and possible_bottom:
                return min(rotations_top, rotations_bottom)
            elif possible_top:
                return rotations_top
            elif possible_bottom:
                return rotations_bottom
            else:
                return -1

        # Check if we can make all tops equal to the first top value
        rotations = check(tops[0], tops, bottoms)
        if rotations != -1:
            return rotations

        # Check if we can make all tops equal to the first bottom value
        rotations = check(bottoms[0], tops, bottoms)
        if rotations != -1:
            return rotations

        return -1

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    tops1 = [2, 1, 2, 4, 2, 2]
    bottoms1 = [5, 2, 6, 2, 3, 2]
    print(f"Min rotations for {tops1}, {bottoms1}: {sol.minDominoRotations(tops1, bottoms1)}")

    tops2 = [3, 5, 1, 2, 3]
    bottoms2 = [3, 6, 3, 3, 4]
    print(f"Min rotations for {tops2}, {bottoms2}: {sol.minDominoRotations(tops2, bottoms2)}")

    tops3 = [1, 2, 1, 1, 1, 2, 2, 2]
    bottoms3 = [2, 1, 2, 2, 2, 1, 1, 2]
    print(f"Min rotations for {tops3}, {bottoms3}: {sol.minDominoRotations(tops3, bottoms3)}")