import ast

class Solution:
    """
    A class containing a method to check if a number can be reordered
    to form a power of two.
    """
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        Determines if a number 'n' can be reordered to form a power of two.

        The approach involves comparing the frequency of digits in 'n' with
        the frequency of digits in all powers of two. If the digit counts match
        for any power of two, it means 'n' can be reordered to form that number.

        Args:
          n: The integer to check.

        Returns:
          True if 'n' can be reordered to form a power of two, False otherwise.
        """
        def count_digits(v: int) -> list[int]:
            """
            Helper function to count the occurrences of each digit (0-9) in a number.
            
            Args:
              v: The integer for which to count digits.
            
            Returns:
              A list of 10 integers, where the index represents the digit
              and the value represents its count.
            """
            digits = [0] * 10
            if v == 0:
                digits[0] = 1
                return digits
            while v > 0:
                digits[v % 10] += 1
                v //= 10
            return digits

        # Get the digit counts for the input number 'n'.
        n_digits = count_digits(n)
        # We also need the number of digits in 'n' for an early exit condition.
        n_total_digit = len(str(n))

        current_power_of_two = 1
        
        # Iterate through powers of two until their number of digits
        # exceeds the number of digits in 'n'.
        while True:
            current_total_digit = len(str(current_power_of_two))
            
            # If the number of digits is the same, we check the digit counts.
            if current_total_digit == n_total_digit:
                # If the digit counts match, we've found a valid reordering.
                if n_digits == count_digits(current_power_of_two):
                    return True
            
            # If the current power of two has more digits than 'n', it's impossible
            # for 'n' to be reordered into this or any larger power of two.
            if current_total_digit > n_total_digit:
                break
            
            # Move to the next power of two.
            current_power_of_two <<= 1
            
        # If the loop finishes without finding a match, no such reordering exists.
        return False

# Example usage with user input
if __name__ == "__main__":
    try:
        # Prompt the user to enter an integer.
        n_input = input("Enter an integer to check if it can be reordered into a power of two: ")
        
        # Safely parse the input string into a Python integer.
        n = int(n_input)
        
        # Instantiate the Solution class.
        solution = Solution()
        
        # Call the method and print the result.
        result = solution.reorderedPowerOf2(n)
        
        print(f"Can {n} be reordered to form a power of two? {result}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
