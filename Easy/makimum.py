class Solution:
    def maximum69Number (self, num: int) -> int:
        """
        Returns the maximum number you can get by changing at most one '6' to a '9'.

        Args:
          num: The input integer.

        Returns:
          The largest possible integer after a single modification.
        """
        # Convert the number to a string for easy manipulation.
        s = str(num)

        # Replace the first occurrence of '6' with '9'.
        # If no '6' exists, the string remains unchanged.
        new_s = s.replace('6', '9', 1)
        
        # Convert the string back to an integer and return it.
        return int(new_s)

# --- Example Usage ---
def get_integer_input(prompt: str) -> int:
    """Helper function to get a validated integer input from the user."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    sol = Solution()
    
    print("--- Maximum 69 Number ---")
    
    num_val = get_integer_input("Enter a number containing digits 6 and/or 9 (e.g., 9669): ")

    result = sol.maximum69Number(num_val)
    print(f"\nThe maximum number is: {result}")
