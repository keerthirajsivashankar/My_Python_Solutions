import ast

class Solution:
  def numberOfWays(self, n: int, x: int) -> int:
    """
    Calculates the number of ways to express 'n' as a sum of unique numbers
    each raised to the power of 'x'.

    This uses a dynamic programming approach with a 1D array `dp`.
    `dp[i]` stores the number of ways to form the number `i`.
    
    The algorithm iterates through all possible numbers `a` and calculates `a^x`.
    For each `a^x`, it updates the `dp` array from `n` down to `a^x`,
    adding the number of ways to form `i - a^x` to `dp[i]`.
    This ensures each number `a^x` is used at most once.

    Args:
      n: The target number to form.
      x: The power to which numbers are raised.

    Returns:
      The total number of unique ways modulo 1,000,000,007.
    """
    MOD = 1_000_000_007
    
    # dp[i] := the number of ways to express i
    # dp[0] is initialized to 1 because there is one way to form 0 (by using no numbers).
    dp = [1] + [0] * n

    # Iterate through numbers 'a' starting from 1.
    for a in range(1, n + 1):
      ax = a**x
      
      # If a^x exceeds n, no further a^x can be used, so we can stop.
      if ax > n:
        break
        
      # Iterate the dp array from n down to ax.
      # This reverse order prevents using the same a^x multiple times
      # in a single calculation (ensuring uniqueness).
      for i in range(n, ax - 1, -1):
        dp[i] += dp[i - ax]
        dp[i] %= MOD

    return dp[n]

if __name__ == "__main__":
    try:
        # Get user input for n and x.
        n_input = input("Enter the target number 'n': ")
        x_input = input("Enter the power 'x': ")
        
        n = int(n_input)
        x = int(x_input)
        
        if n < 0 or x < 0:
            print("n and x must be non-negative integers.")
        else:
            # Create an instance of the Solution class.
            solution = Solution()
            
            # Call the method and print the result.
            result = solution.numberOfWays(n, x)
            
            print(f"The number of ways to express {n} is: {result}")
    
    except ValueError:
        print("Invalid input. Please enter valid integers for n and x.")
