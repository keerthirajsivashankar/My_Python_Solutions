import collections
from typing import List

class Solution:
  def minCost(self, basket1: List[int], basket2: List[int]) -> int:
    swapped = []
    
    # Count the frequency of each number across both baskets.
    # The result shows the imbalance: a positive frequency means a number
    # is more common in basket1, a negative frequency means it's more common in basket2.
    count = collections.Counter(basket1)
    count.subtract(collections.Counter(basket2))

    # Check if the baskets can be made equal.
    # For baskets to be equal, the total count of each number must be even.
    # If any number has an odd frequency difference, a simple swap won't fix it.
    for num, freq in count.items():
      if freq % 2 != 0:
        return -1
      
      # Add numbers that need to be swapped to a list.
      # `abs(freq // 2)` gives the number of items that must be moved.
      swapped += [num] * abs(freq // 2)

    # Sort the list of numbers that need to be moved.
    swapped.sort()
    
    # Find the global minimum cost of a single item in either basket.
    minNum = min(min(basket1), min(basket2))
    
    # Calculate the minimum cost.
    # The items to be swapped are split into two groups: the smaller half and the larger half.
    # The number of swaps is `len(swapped) // 2`.
    # For each swap, the cost is either the direct swap of two cheapest items (from the `swapped` list)
    # or an indirect swap using the global minimum element (`minNum`) as an intermediary,
    # which costs `2 * minNum`. We take the minimum of these options for each swap.
    return sum(min(2 * minNum, num) for num in swapped[0:len(swapped) // 2])

def get_list_of_integers_input(prompt: str, required_len: int = -1) -> List[int]:
    while True:
        try:
            input_str = input(prompt)
            elements = [int(x) for x in input_str.split()]
            if not elements:
                print("List cannot be empty. Please enter at least one integer.")
            elif required_len != -1 and len(elements) != required_len:
                print(f"The list must have {required_len} elements. Please re-enter.")
            else:
                return elements
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    sol = Solution()
    
    print("--- Minimum Cost to Make All Baskets Equal ---")
    
    basket1_val = get_list_of_integers_input("Enter numbers for basket1 (e.g., '4 2 2 2'): ")
    
    basket2_val = get_list_of_integers_input(
        f"Enter numbers for basket2 (must have {len(basket1_val)} elements) (e.g., '1 4 1 2'): ", 
        required_len=len(basket1_val)
    )

    result = sol.minCost(basket1_val, basket2_val)
    print(f"\nThe minimum cost to make the baskets equal is: {result}")