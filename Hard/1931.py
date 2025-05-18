from collections import defaultdict
from typing import List, Tuple

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        """
        Calculates the number of ways to color an m x n grid with 3 colors
        such that no two adjacent cells have the same color.

        Args:
            m: The number of rows in the grid.
            n: The number of columns in the grid.

        Returns:
            The number of valid colorings modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        # Generate all valid row colorings
        def generate_valid_rows(n: int) -> List[Tuple[int, ...]]:
            """
            Generates all possible valid colorings for a single row.
            A row coloring is valid if no two adjacent cells have the same color.

            Args:
                n: The number of columns in the row.

            Returns:
                A list of tuples, where each tuple represents a valid row coloring.
                Each element in the tuple is an integer representing the color (0, 1, or 2).
            """
            valid_rows: List[Tuple[int, ...]] = []

            def backtrack(pos: int, path: List[int]) -> None:
                """
                Recursive backtracking function to generate valid row colorings.

                Args:
                    pos: The current column position being colored.
                    path: The current color sequence for the row.
                """
                if pos == n:
                    valid_rows.append(tuple(path))  # Convert list to tuple for immutability
                    return
                for color in range(3):
                    if pos == 0 or color != path[-1]:  # Check adjacent color constraint
                        path.append(color)
                        backtrack(pos + 1, path)
                        path.pop()  # Backtrack: remove the last color to try others

            backtrack(0, [])
            return valid_rows

        # Build compatibility map
        def build_compatibility(valid_rows: List[Tuple[int, ...]]) -> defaultdict[int, List[int]]:
            """
            Builds a dictionary (compatibility map) indicating which row colorings
            can be adjacent to each other in the grid.

            Args:
                valid_rows: A list of valid row colorings.

            Returns:
                A dictionary where keys are row indices and values are lists of
                indices of compatible rows.  Two rows are compatible if no
                corresponding cells have the same color.
            """
            compat: defaultdict[int, List[int]] = defaultdict(list)
            for i, row1 in enumerate(valid_rows):
                for j, row2 in enumerate(valid_rows):
                    if all(c1 != c2 for c1, c2 in zip(row1, row2)):  # Check column-wise constraint
                        compat[i].append(j)
            return compat

        valid_rows = generate_valid_rows(n)
        compat = build_compatibility(valid_rows)

        # dp[i] := number of ways to color the grid up to the current row, ending with row valid_rows[i]
        dp: List[int] = [1] * len(valid_rows)  # Initialize: Each row can be the first row

        for _ in range(m - 1):  # Iterate through remaining rows (m-1)
            new_dp: List[int] = [0] * len(valid_rows)
            for i, count in enumerate(dp):  # For each way to color up to the previous row ending in row i
                for j in compat[i]:  # For each row j compatible with row i
                    new_dp[j] = (new_dp[j] + count) % MOD  # Add the number of ways to reach row i
            dp = new_dp  # Update dp for the next row

        return sum(dp) % MOD  # Sum up the ways to color the grid ending in each valid row.
