import math
from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        """
        Finds the area of the rectangle with the largest diagonal from a list of dimensions.

        Args:
            dimensions: A list of lists, where each inner list [l, b]
                        represents the length and width of a rectangle.

        Returns:
            The area of the rectangle with the maximum diagonal.
        """
        max_area = 0
        max_diagonal_sq = 0  # We can compare the square of the diagonal to avoid floating point issues

        # Iterate through each rectangle's dimensions
        for l, b in dimensions:
            # Calculate the diagonal squared (l^2 + b^2).
            # We don't need to take the square root for comparison, as if a > b, then a^2 > b^2 for positive numbers.
            current_diagonal_sq = (l * l) + (b * b)

            # Check if the current diagonal is the new maximum.
            # If diagonals are equal, the one with the greater area takes precedence.
            if current_diagonal_sq > max_diagonal_sq:
                # If it's a new max diagonal, update both the max diagonal and the max area.
                max_diagonal_sq = current_diagonal_sq
                max_area = (l * b)
            # Handle the tie-breaker case where diagonals are equal.
            elif current_diagonal_sq == max_diagonal_sq:
                # If diagonals are the same, update the area only if the current area is larger.
                max_area = max(max_area, l * b)

        return max_area

# --- Example Usage ---
def get_dimensions_input() -> List[List[int]]:
    """Helper function to get dimensions from user input."""
    while True:
        try:
            input_str = input("Enter dimensions as a list of lists (e.g., '[[9,3],[8,6]]'): ")
            # Use a safe way to evaluate the input string as a Python literal
            dimensions_list = eval(input_str)
            
            # Validate the format
            if not isinstance(dimensions_list, list) or not all(isinstance(dim, list) and len(dim) == 2 and all(isinstance(val, int) and val > 0 for val in dim) for dim in dimensions_list):
                print("Invalid format. Please enter a list of lists with two positive integers each.")
                continue
            
            return dimensions_list
        except (SyntaxError, ValueError, IndexError):
            print("Invalid input format. Please enter a valid list of lists, like '[[9,3],[8,6]]'.")

if __name__ == "__main__":
    solution = Solution()
    
    print("--- Area of Rectangle with Maximum Diagonal ---")
    
    dimensions_val = get_dimensions_input()
    result = solution.areaOfMaxDiagonal(dimensions_val)
    print(f"\nThe area of the rectangle with the maximum diagonal is: {result}")
