import sys

class Solution:
  def new21Game(self, n: int, k: int, maxPts: int) -> float:
    """
    Calculates the probability of getting a score less than or equal to n
    in the New 21 Game.

    Args:
      n: The maximum score allowed.
      k: The score at which drawing stops.
      maxPts: The number of cards in the deck, from 1 to maxPts.

    Returns:
      The probability as a float.
    """
    # A simplified case: If k is 0, the game ends immediately with 0 points,
    # and we meet the n >= 0 condition.
    # Also, if n is large enough to cover all possible point totals (k-1 + maxPts),
    # the probability of winning is 100%.
    if k == 0 or n >= k - 1 + maxPts:
      return 1.0

    # 'dp' array stores the probability of having a certain score 'i'.
    # dp[i] = P(score == i)
    dp = [1.0] + [0] * n
    
    # 'windowSum' is the sum of probabilities P(i - 1) + ... + P(i - maxPts).
    # This is used to efficiently calculate the next probability.
    windowSum = dp[0]

    # 'ans' stores the total probability of winning, which is the sum of
    # probabilities for scores from k to n.
    ans = 0.0

    # Iterate from a score of 1 up to n.
    for i in range(1, n + 1):
      # The probability of reaching score 'i' is the sum of probabilities of all
      # previous scores from which we could draw to get to 'i', divided by maxPts.
      dp[i] = windowSum / maxPts
      
      # If the current score is less than k, the game continues. We add the new
      # probability dp[i] to our sliding window sum.
      if i < k:
        windowSum += dp[i]
      # If the current score is k or more, the game ends. We add the new
      # probability dp[i] to our final answer.
      else:
        ans += dp[i]
      
      # Now, we need to "slide the window" by removing the probability
      # of the oldest score (i - maxPts). This keeps our windowSum up to date.
      if i - maxPts >= 0:
        windowSum -= dp[i - maxPts]

    return ans

if __name__ == "__main__":
    solution = Solution()

    # --- User Input Section ---
    try:
        n_input = int(input("Enter n (the max score allowed): "))
        k_input = int(input("Enter k (the score to stop drawing): "))
        maxPts_input = int(input("Enter maxPts (the number of cards): "))
        
        # Validate that the inputs are positive integers.
        if n_input < 0 or k_input < 0 or maxPts_input <= 0:
            print("Inputs n and k must be non-negative, and maxPts must be positive.")
        else:
            result = solution.new21Game(n_input, k_input, maxPts_input)
            print(f"\nThe probability of winning the New 21 Game is: {result:.5f}")

    except ValueError:
        print("Invalid input. Please enter valid integers for n, k, and maxPts.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
