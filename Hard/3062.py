from typing import List

class Solution:
  def maximumValueSum(
      self,
      nums: List[int],
      k: int,
      edges: List[List[int]], # This parameter is present in the signature but not used in the logic.
  ) -> int:
    """
    Calculates the maximum possible sum of elements in `nums` after
    applying an XOR operation with `k` to some elements.
    The goal is to maximize the sum, subject to an implicit constraint
    (often related to graph parity) that leads to needing an even number of XOR operations.

    Args:
      nums: A list of integers.
      k: The integer to XOR with.
      edges: A list of edges. This parameter is present in the method signature
             but is not used in the provided implementation's logic.

    Returns:
      The maximum possible sum.
    """
    
    # Initial strategy: For each number, choose the maximum of (original num) or (num ^ k).
    # This gives the absolute maximum sum if there were no parity constraints.
    maxSum = sum(max(num, num ^ k) for num in nums)

    # Count how many numbers actually increased their value by applying XOR with k.
    # These are the numbers for which (num ^ k) > num.
    changedCount = sum((num ^ k) > num for num in nums)

    # If the count of numbers that benefited from XOR is even, then `maxSum` is valid.
    # This is because we implicitly chose to XOR an even number of elements that increased their value.
    if changedCount % 2 == 0:
      return maxSum
    
    # If `changedCount` is odd, we cannot achieve `maxSum` directly
    # because we need an even number of XOR operations (implied by the problem context
    # that usually comes with this specific constraint, often related to tree properties).
    #
    # To satisfy the even parity, we must "undo" one XOR operation (if it increased value)
    # or "add" one XOR operation (if it decreased value) to maintain the overall parity.
    #
    # We want to minimize the reduction from `maxSum`.
    # This means we need to find the smallest absolute difference |num - (num ^ k)|.
    #
    # Case 1: We must "undo" one of the beneficial XOR operations.
    #   This means we had `num ^ k` but now must use `num`. The loss is `(num ^ k) - num`.
    #
    # Case 2: We must "add" an XOR operation to a number that previously preferred `num`.
    #   This means we had `num` but now must use `num ^ k`. The loss is `num - (num ^ k)`.
    #   Note: If `num ^ k` was smaller, then `num - (num ^ k)` is positive, representing a reduction.
    #
    # In both cases, the *cost* or *reduction* from `maxSum` is `abs(num - (num ^ k))`.
    # We choose the minimum such reduction.
    minChangeDiff = float('inf') # Initialize with a very large value

    for num in nums:
        # Calculate the absolute difference between num and num ^ k.
        # This represents the "cost" of toggling the XOR state for this number
        # from its locally optimal choice to the other state, to satisfy parity.
        diff = abs(num - (num ^ k))
        minChangeDiff = min(minChangeDiff, diff)
        
    return maxSum - minChangeDiff