from collections import defaultdict
import ast

class Solution:
    """
    A class to solve the "Fruit Into Baskets" problem.
    The problem is to find the length of the longest subarray with at most two distinct numbers.
    """
    def totalFruit(self, fruits: list[int]) -> int:
        """
        Calculates the maximum number of fruits that can be collected from two baskets.

        This function uses a sliding window approach. It expands the window from the right
        and shrinks it from the left whenever the number of distinct fruit types exceeds two.

        Args:
            fruits: A list of integers representing the type of fruit in each tree.

        Returns:
            The maximum number of fruits that can be collected.
        """
        l = 0
        count = defaultdict(int)
        max_len = 0

        # Iterate through the fruits with the right pointer
        for r in range(len(fruits)):
            # Add the current fruit to the window
            count[fruits[r]] += 1

            # If the number of distinct fruit types is more than 2,
            # shrink the window from the left until it's valid again
            while len(count) > 2:
                count[fruits[l]] -= 1
                # If the count of the leftmost fruit becomes 0, remove it from the dictionary
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                # Move the left pointer to the right
                l += 1

            # Update the maximum length of the valid window
            max_len = max(max_len, r - l + 1)

        return max_len

if __name__ == "__main__":
    try:
        # Prompt the user for input
        fruits_input = input("Enter a list of fruit types (e.g., [1,2,1,3,4,3,2]): ")

        # Safely evaluate the input string as a Python literal
        fruits_list = ast.literal_eval(fruits_input)
        
        # Instantiate the Solution class
        solution = Solution()
        
        # Call the totalFruit method and get the result
        result = solution.totalFruit(fruits_list)
        
        # Print the final result to the user
        print(f"The maximum number of fruits that can be collected is: {result}")
        
    except (ValueError, SyntaxError) as e:
        print(f"Invalid input: {e}")
        print("Please ensure your input is a valid Python list of integers, like [1, 2, 3, 2, 1].")

