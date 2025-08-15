import sys

class Solution:
    """
    A class containing a method to check if a number is a power of four.
    """
    def isPowerOfFour(self, n: int) -> bool:
        """
        Determines if an integer 'n' is a power of four.

        The approach is to handle edge cases first, then repeatedly divide 'n'
        by 4 as long as it's perfectly divisible. If the final number is 1,
        it means the original number was a power of four.

        Args:
          n: The integer to check.

        Returns:
          True if n is a power of four, False otherwise.
        """
        # A power of four must be a positive integer.
        if n <= 0:
            return False

        # Repeatedly divide n by 4 as long as the remainder is 0.
        while n % 4 == 0:
            n //= 4

        # If the final result is 1, it means the original number
        # was a power of four. Otherwise, it wasn't.
        return n == 1

if __name__ == "__main__":
    solution = Solution()

    # Get user input.
    try:
        user_input_str = input("Enter an integer to check if it's a power of four: ")
        n = int(user_input_str)
        result = solution.isPowerOfFour(n)
        print(f"Is {n} a power of four? {result}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
