from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        Traverses a 2D matrix in a diagonal order and returns the elements
        as a 1D list.

        This approach uses a dictionary or a list of lists to group elements
        by the sum of their row and column indices (r + c), which is constant
        for each diagonal.

        Args:
          mat: A 2D list of integers.

        Returns:
          A 1D list containing the elements in diagonal order.
        """
        # Get the dimensions of the matrix.
        rows, cols = len(mat), len(mat[0])

        # Create a list of lists to hold the elements of each diagonal.
        # The number of diagonals is `rows + cols - 1`.
        diagonals = [[] for _ in range(rows + cols - 1)]

        # Iterate through the matrix and group elements into their respective diagonals.
        for r in range(rows):
            for c in range(cols):
                # The sum of row and column indices (r + c) determines the diagonal group.
                diagonals[r + c].append(mat[r][c])

        ans = []
        # This flag helps us alternate between normal and reversed order for each diagonal.
        need_reversed = 1

        # Iterate through the diagonals and append them to the final result list.
        for diagonal in diagonals:
            if need_reversed:
                # For odd-indexed diagonals (0, 2, 4...), reverse the list.
                # In the problem, these correspond to upward-moving diagonals.
                ans.extend(diagonal[::-1])
            else:
                # For even-indexed diagonals (1, 3, 5...), add them in the original order.
                # These correspond to downward-moving diagonals.
                ans.extend(diagonal[:])

            # Toggle the flag for the next diagonal.
            need_reversed = 1 - need_reversed
        
        return ans

# --- Example Usage ---
def get_matrix_input(prompt: str) -> List[List[int]]:
    """Helper function to get a matrix from the user."""
    while True:
        try:
            print(prompt)
            rows = []
            while True:
                row_str = input("Enter a row of integers (e.g., '1 2 3') or leave empty to finish: ")
                if not row_str:
                    break
                row = [int(x) for x in row_str.split()]
                rows.append(row)

            if not rows or all(len(row) == len(rows[0]) for row in rows):
                return rows
            else:
                print("All rows must have the same number of elements.")
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")

if __name__ == "__main__":
    sol = Solution()
    
    print("--- Diagonal Matrix Traversal ---")
    
    matrix_val = get_matrix_input("Enter a matrix row by row:")
    
    if not matrix_val:
        print("No matrix provided.")
    else:
        result = sol.findDiagonalOrder(matrix_val)
        print(f"\nThe diagonal order of the matrix is: {result}")
