import sys
import ast

class Solution:
    """
    A class containing a method to check if a number is a power of two.
    """
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Determines if an integer is a power of two.

        This method works by converting the integer to its binary representation
        and checking if the count of '1's is exactly one. This is a correct
        and intuitive approach.

        A more common and slightly more efficient approach for this problem
        is using bitwise operations: `return n > 0 and (n & (n - 1)) == 0`.
        A number is a power of two if and only if it is positive and has
        only one bit set to 1. The expression `n & (n - 1)` unsets the
        least significant bit, so if `n` has only one '1', the result will be 0.

        Args:
          n: The integer to check.

        Returns:
          True if n is a power of two, False otherwise.
        """
        # A power of two must be a positive integer.
        if n <= 0:
            return False

        # Convert the number to its binary string representation.
        b = bin(n)
        
        # Count the number of '1's in the binary string.
        res = b.count("1")

        # A number is a power of two if and only if its binary representation
        # contains exactly one '1'.
        return True if res == 1 else False

# Example usage with user input
if __name__ == "__main__":
    try:
        # Prompt the user to enter an integer.
        n_input = input("Enter an integer to check if it's a power of two: ")
        
        # Safely parse the input string into a Python integer.
        n = int(n_input)
        
        # Create an instance of the Solution class.
        solution = Solution()
        
        # Call the method and print the result.
        result = solution.isPowerOfTwo(n)
        
        print(f"Is {n} a power of two? {result}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
