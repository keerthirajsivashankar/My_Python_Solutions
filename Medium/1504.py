from typing import List

class Solution:
  def numSubmat(self, mat: List[List[int]]) -> int:
    """
    Counts the number of submatrices with all ones using an optimized dynamic programming
    approach. This solution has a time complexity of O(m * n).

    Args:
      mat: The input matrix of 0s and 1s.

    Returns:
      The total count of all-ones submatrices.
    """
    m = len(mat)
    n = len(mat[0])
    ans = 0
    # The 'histogram' array will store the number of consecutive ones above each cell.
    histogram = [0] * n

    # We iterate through the matrix row by row.
    for i in range(m):
      # For each row, we first build the current histogram.
      for j in range(n):
        if mat[i][j] == 1:
          # If the current cell is 1, we extend the height of the histogram.
          histogram[j] += 1
        else:
          # If the current cell is 0, the consecutive ones streak is broken,
          # so we reset the height to 0.
          histogram[j] = 0
      
      # Now, for the current histogram (the `histogram` array), we can calculate
      # the number of all-ones submatrices that have their bottom row at `i`.
      # We use a helper function to perform this calculation.
      ans += self._count_subarrays(histogram)

    return ans

  def _count_subarrays(self, row: List[int]) -> int:
    """
    Counts the number of all-ones subarrays in a single row (or histogram).
    This linear scan approach is highly efficient for this specific counting task.

    Args:
      row: A list representing a histogram of consecutive ones.

    Returns:
      The total number of all-ones subarrays in that row.
    """
    res = 0
    length = 0
    for num in row:
      # If we encounter a zero, the streak of ones is broken.
      length = 0 if num == 0 else length + 1
      # For each position, the number of subarrays ending there is equal
      # to the length of the consecutive ones streak. We add this to the total.
      res += length
    return res

# --- Example Usage ---
def get_matrix_input(prompt: str) -> List[List[int]]:
    """Helper function to get a binary matrix from the user."""
    while True:
        try:
            print(prompt)
            rows = []
            while True:
                row_str = input("Enter a row (e.g., '1 0 1') or leave empty to finish: ")
                if not row_str:
                    break
                row = [int(x) for x in row_str.split()]
                if not all(x in [0, 1] for x in row):
                    print("Row must contain only 0s and 1s. Please try again.")
                    continue
                rows.append(row)

            if not rows or all(len(row) == len(rows[0]) for row in rows):
                return rows
            else:
                print("All rows must have the same number of elements.")
        except ValueError:
            print("Invalid input. Please enter 0s and 1s separated by spaces.")

if __name__ == "__main__":
    sol = Solution()
    
    print("--- Optimized All-Ones Submatrix Counter ---")
    
    matrix_val = get_matrix_input("Enter a binary matrix (0s and 1s) row by row:")
    
    if not matrix_val:
        print("No matrix provided.")
    else:
        result = sol.numSubmat(matrix_val)
        print(f"\nFor the given matrix, the total number of all-ones submatrices is: {result}")
