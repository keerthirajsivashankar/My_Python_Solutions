import sys

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """
        Finds the largest "good" integer from a string of digits.
        A "good" integer is a substring of length three with identical digits.

        Args:
          num: A string of digits.

        Returns:
          The largest good integer as a string, or an empty string if none exists.
        """
        max_good_integer_str = ""
        
        # Iterate through the string, checking for substrings of length 3.
        # We stop at len(num) - 2 to avoid an index out of bounds error.
        for i in range(len(num) - 2):
            # Check if three consecutive digits are the same.
            if num[i] == num[i+1] == num[i+2]:
                # If a good integer is found, it's the current substring.
                current_good_integer_str = num[i:i+3]
                
                # Check if this is the first one, or if it's larger than the current max.
                # String comparison works perfectly here: "999" > "888".
                if current_good_integer_str > max_good_integer_str:
                    max_good_integer_str = current_good_integer_str
        
        return max_good_integer_str

if __name__ == "__main__":
    solution = Solution()

    # Get user input.
    try:
        user_input_str = input("Enter a string of digits: ")
        result = solution.largestGoodInteger(user_input_str)
        print(f"The largest good integer is: '{result}'")
    except Exception as e:
        print(f"An error occurred: {e}")
