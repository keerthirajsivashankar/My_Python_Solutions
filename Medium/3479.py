import ast

class Solution:
  def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
    """
    Calculates the number of fruits that cannot be placed into baskets
    using a segment tree for efficient basket allocation.

    The segment tree stores the maximum capacity in ranges of baskets,
    allowing for quick queries to find the leftmost available basket
    that can hold a given fruit.

    Args:
      fruits: A list of integers representing the size of each fruit.
      baskets: A list of integers representing the capacity of each basket.

    Returns:
      The total number of fruits that could not be placed.
    """
    n = len(baskets)
    
    # Calculate N: the smallest power of 2 greater than or equal to n.
    # This is used to size the segment tree array for convenience.
    N = 1
    while N < n: # Changed N <= n to N < n to ensure N is strictly greater if n is a power of 2
        N <<= 1
    
    # Initialize the segment tree array. It will have size 2*N.
    # The leaves (original basket capacities) will be stored from index N to 2*N-1.
    segTree = [0] * (2 * N)
    
    # Populate the leaf nodes of the segment tree with basket capacities.
    # Baskets are placed at indices N, N+1, ..., N+n-1.
    for i in range(n):
        segTree[N + i] = baskets[i]
    
    # Build the segment tree from bottom-up.
    # Each parent node stores the maximum value of its children.
    for i in range(N - 1, 0, -1):
        segTree[i] = max(segTree[2 * i], segTree[2 * i + 1])
    
    count = 0 # Counter for unplaced fruits

    # Iterate through each fruit in the given order.
    for fruit in fruits:
        index = 1 # Start at the root of the segment tree.
        
        # Check if even the largest available basket (max capacity in the whole tree)
        # can hold the current fruit. If not, this fruit cannot be placed.
        if segTree[index] < fruit:
            count += 1
            continue # Move to the next fruit.
        
        # Traverse down the segment tree to find the leftmost suitable basket.
        while index < N: # Continue until a leaf node is reached (index >= N)
            # If the left child's segment (representing the left half of the current range)
            # has a maximum capacity greater than or equal to the fruit, go left.
            # This prioritizes the leftmost available basket.
            if segTree[2 * index] >= fruit:
                index = 2 * index
            # Otherwise, the left segment cannot hold the fruit, so we must go right.
            else:
                index = 2 * index + 1
        
        # At this point, 'index' is the leaf node corresponding to the chosen basket.
        # Mark this basket as used by setting its capacity to -1.
        # This makes it unavailable for future fruits and correctly propagates up
        # in the max calculations.
        segTree[index] = -1
        
        # Update the segment tree from the leaf node up to the root.
        # This ensures that parent nodes reflect the new maximums after a basket is used.
        while index > 1:
            index //= 2 # Move to the parent node.
            # The parent's max is the maximum of its two children.
            segTree[index] = max(segTree[2 * index], segTree[2 * index + 1])
        
    return count # Return the total number of fruits that could not be placed.

if __name__ == "__main__":
  try:
    # Get user input for fruits and baskets.
    fruits_input = input("Enter a list of fruit sizes (e.g., [4, 2, 5]): ")
    baskets_input = input("Enter a list of basket capacities (e.g., [3, 5, 4]): ")
    
    # Safely parse the string input into Python lists.
    fruits_list = ast.literal_eval(fruits_input)
    baskets_list = ast.literal_eval(baskets_input)
    
    # Instantiate the Solution class.
    solution = Solution()
    
    # Call the function and print the result.
    unplaced_count = solution.numOfUnplacedFruits(fruits_list, baskets_list)
    
    print(f"Number of unplaced fruits: {unplaced_count}")

  except (ValueError, SyntaxError) as e:
    print(f"Invalid input: {e}")
    print("Please ensure your input is a valid Python list of integers.")
