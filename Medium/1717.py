from typing import List

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        def solve(text: str, pattern: str, score: int):
            stack = []
            points = 0
            for char in text:
                # If stack is not empty and the current char matches pattern[1]
                # and the last char in stack matches pattern[0], we found a pair.
                if stack and stack[-1] == pattern[0] and char == pattern[1]:
                    stack.pop() # Remove the pattern[0] character
                    points += score # Add the score
                else:
                    # If no pair is formed, add the current character to the stack
                    stack.append(char)
            return points, "".join(stack) # Return accumulated points and remaining string

        # Determine the order of operations based on which substring gives more points
        if x >= y:
            # Prioritize 'ab' if its score is greater than or equal to 'ba''s score
            points1, remaining_s = solve(s, "ab", x)
            # After removing all possible 'ab's, process the remaining string for 'ba's
            points2, _ = solve(remaining_s, "ba", y)
        else:
            # Prioritize 'ba' if its score is greater than 'ab''s score
            points1, remaining_s = solve(s, "ba", y)
            # After removing all possible 'ba's, process the remaining string for 'ab's
            points2, _ = solve(remaining_s, "ab", x)
            
        # The total maximum gain is the sum of points from both passes
        return points1 + points2

def get_string_input(prompt: str) -> str:
    while True:
        s_val = input(prompt)
        # Validate that the input string only contains 'a' and 'b' characters
        if all(char in 'ab' for char in s_val):
            return s_val
        else:
            print("Invalid input. Please enter a string containing only 'a' and 'b' characters.")

def get_integer_input(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    sol = Solution()
    
    print("--- Maximum Score From Removing Substrings ---")
    
    # Get user inputs for the string and scores
    s_val = get_string_input("Enter the string s (e.g., 'cdbaab'): ")
    x_val = get_integer_input("Enter the score for 'ab' (x): ")
    y_val = get_integer_input("Enter the score for 'ba' (y): ")

    # Calculate and print the result
    result = sol.maximumGain(s_val, x_val, y_val)
    print(f"\nThe maximum score that can be obtained is: {result}")