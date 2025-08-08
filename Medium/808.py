import functools
import sys

# It's good practice to increase the recursion limit for deep recursive calls,
# which can happen with large `n` values in this problem.
sys.setrecursionlimit(2000)

class Solution:
    def soupServings(self, n: int) -> float:
        """
        Calculates the probability that soup A runs out first, given initial amounts of soup A and B.

        This problem is solved using dynamic programming with memoization.
        We model the problem as a recursive function `dfs(a, b)` which returns the probability
        of A running out first, given 'a' servings of soup A and 'b' servings of soup B.

        The problem has a special property: for very large `n`, the probability approaches 1.
        We can use an optimization to return 1.0 immediately for `n` greater than a certain threshold.
        4800 is a safe threshold based on the problem's constraints and behavior.

        Args:
          n: The initial amount of soup in milliliters (ml).

        Returns:
          The probability that soup A runs out first.
        """

        # Optimization: For very large 'n', the probability that soup A runs out first
        # becomes extremely close to 1. We can return 1.0 directly to save time.
        # The value 4800 is a commonly used threshold for this problem.
        if n >= 4800:
            return 1.0

        # We normalize the amounts by dividing by 25ml, which is the smallest serving size.
        # `(n + 24) // 25` is a way to calculate ceil(n / 25).
        # This converts the problem from ml to discrete "servings" of 25ml.
        a = (n + 24) // 25
        b = (n + 24) // 25

        @functools.lru_cache(None)
        def dfs(a_servings: int, b_servings: int) -> float:
            """
            Recursive function with memoization to find the probability.
            a_servings: Number of 25ml servings of soup A.
            b_servings: Number of 25ml servings of soup B.
            """
            # Base Case 1: If both soups are depleted (or <= 0), the probability of
            # A running out first is 0.5 (as they run out at the same time).
            if a_servings <= 0 and b_servings <= 0:
                return 0.5
            
            # Base Case 2: If soup A is depleted first, the probability is 1.0.
            if a_servings <= 0:
                return 1.0
            
            # Base Case 3: If soup B is depleted first, the probability of A being first is 0.0.
            if b_servings <= 0:
                return 0.0
            
            # Recursive Step: We have four possible servings, each with a 25% probability.
            # We calculate the probability for each of the four new states and sum them up.
            return 0.25 * (
                dfs(a_servings - 4, b_servings) +
                dfs(a_servings - 3, b_servings - 1) +
                dfs(a_servings - 2, b_servings - 2) +
                dfs(a_servings - 1, b_servings - 3)
            )

        # Start the recursive calls with the initial number of servings.
        return dfs(a, b)

# Example usage with user input
if __name__ == "__main__":
    try:
        n_input = input("Enter the total amount of soup in ml (n): ")
        n = int(n_input)
        
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            solution = Solution()
            result = solution.soupServings(n)
            print(f"The probability that soup A runs out first is: {result}")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
