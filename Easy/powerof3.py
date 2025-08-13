import ast

class Solution:
    """
    A class containing a method to check if a number is a power of three.
    """
    def isPowerOfThree(self, n: int) -> bool:
        """
        Determines if an integer 'n' is a power of three.

        The approach is to handle edge cases first, then repeatedly divide 'n'
        by 3 as long as it's perfectly divisible. If the final number is 1,
        it means the original number was a power of three.

        Args:
          n: The integer to check.

        Returns:
          True if n is a power of three, False otherwise.
        """
        # A power of three must be a positive integer.
        if n <= 0:
            return False
        
        # 3^0 is 1, so this is a valid base case.
        if n == 1:
            return True

        # Keep dividing n by 3 as long as it's perfectly divisible.
        while n % 3 == 0:
            n //= 3
            
        # If the final result is 1, it means the original number
        # was a power of three. Otherwise, it wasn't.
        return n == 1

# Example usage with user input
if __name__ == "__main__":
    try:
        # Prompt the user to enter an integer.
        n_input = input("Enter an integer to check if it's a power of three: ")
        
        # Safely parse the input string into a Python integer.
        n = int(n_input)
        
        # Create an instance of the Solution class.
        solution = Solution()
        
        # Call the method and print the result.
        result = solution.isPowerOfThree(n)
        
        print(f"Is {n} a power of three? {result}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
