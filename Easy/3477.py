import ast

class Solution:
  def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
    """
    Calculates the number of fruits that cannot be placed into baskets,
    following the "left-to-right" and "leftmost available basket" rules.

    Args:
      fruits: A list of integers representing the size of each fruit.
      baskets: A list of integers representing the capacity of each basket.

    Returns:
      The total number of fruits that could not be placed.
    """
    n = len(fruits)
    num_unplaced_fruits = 0
    
    # We use a boolean list to track which baskets have been used.
    # This is more explicit than overwriting the list with zeros.
    baskets_used = [False] * len(baskets)

    # Iterate through the fruits in the specified left-to-right order.
    for i in range(n):
      fruit_placed = False
      
      # For each fruit, iterate through the baskets to find the leftmost available one.
      for j in range(len(baskets)):
        # Check if the basket is not used and has enough capacity.
        if not baskets_used[j] and fruits[i] <= baskets[j]:
          # This is the leftmost valid basket, so we place the fruit here.
          baskets_used[j] = True
          fruit_placed = True
          break  # Exit the inner loop to move to the next fruit.
      
      # If the fruit was not placed after checking all baskets, increment the count.
      if not fruit_placed:
        num_unplaced_fruits += 1
        
    return num_unplaced_fruits

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
