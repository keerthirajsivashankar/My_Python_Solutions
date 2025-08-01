from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Generates Pascal's Triangle up to a specified number of rows.
        """
        n = numRows
        
        def binomial(n: int, k: int) -> int:
            """
            Calculates the binomial coefficient "n choose k" (C(n, k)).
            It uses an optimized iterative approach to avoid large intermediate numbers.
            """
            res = 1
            # Optimization: C(n, k) is the same as C(n, n-k).
            # We choose the smaller k to perform fewer multiplications.
            if k > n - k:
                k = n - k
            
            # Calculate C(n, k) = (n * (n-1) * ... * (n-k+1)) / (k * (k-1) * ... * 1)
            for i in range(k):
                res *= (n - i)
                res //= (i + 1) # Use integer division
            return res
            
        mat = [] # This will store Pascal's Triangle

        # Loop through each row from 0 to n-1
        for i in range(n):
            arr = [] # This will store the elements of the current row
            # Loop through each element in the current row from 0 to i
            for j in range(i + 1):
                # The value at row 'i' and position 'j' is C(i, j)
                arr.append(binomial(i, j))
            mat.append(arr)
        
        return mat

def get_integer_input(prompt: str, min_val: int = 0) -> int:
    """Helper function to get a validated integer input from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value >= min_val:
                return value
            else:
                print(f"Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    sol = Solution()
    
    print("--- Pascal's Triangle Generator ---")
    
    num_rows_val = get_integer_input("Enter the number of rows for Pascal's Triangle: ")

    result = sol.generate(num_rows_val)
    
    print(f"\nPascal's Triangle with {num_rows_val} rows:")
    for row_idx, row in enumerate(result):
        print(f"Row {row_idx}: {' '.join(map(str, row))}")