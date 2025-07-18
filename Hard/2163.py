import heapq
import math
from typing import List

class Solution:
  def minimumDifference(self, nums: List[int]) -> int:
    n = len(nums) // 3
    ans = math.inf
    leftSum = 0
    rightSum = 0
    maxHeap = []  # Stores largest 'n' elements from the left, to find minimum sum
    minHeap = []  # Stores smallest 'n' elements from the right, to find maximum sum
    
    # minLeftSum[i] stores the minimum sum of 'n' elements chosen from nums[0...i]
    # where 'i' is the index of the last element considered for the left partition.
    # The size of minLeftSum should be len(nums).
    minLeftSum = [0] * len(nums)

    # Calculate minLeftSum for all possible ending points of the left partition
    # The left partition will always have 'n' elements.
    # We iterate up to 2*n because the left partition can end at index 2*n - 1.
    for i in range(2 * n):
      # Push negative of current number to maxHeap to simulate a min-heap behavior
      # for finding the 'n' smallest elements (by keeping n largest negative values)
      heapq.heappush(maxHeap, -nums[i])
      leftSum += nums[i]
      
      # If heap size exceeds 'n', remove the largest element (smallest negative)
      # This ensures maxHeap always contains the 'n' smallest elements encountered so far
      if len(maxHeap) == n + 1:
        leftSum += heapq.heappop(maxHeap) # Add back the popped negative value (subtracts original value)
      
      # When maxHeap has exactly 'n' elements, leftSum is the sum of these 'n' smallest elements
      # ending at index 'i'.
      if len(maxHeap) == n:
        minLeftSum[i] = leftSum

    # Calculate the minimum difference by iterating from right to left
    # The right partition will also have 'n' elements.
    # The middle element will be at index 'i-1' after the right partition.
    # We iterate from the end of the array down to index 'n' (inclusive).
    # The loop `range(len(nums) - 1, n - 1, -1)` correctly covers indices from `3*n - 1` down to `n`.
    for i in range(len(nums) - 1, n - 1, -1):
      # Push current number to minHeap to find the 'n' largest elements for the right sum
      heapq.heappush(minHeap, nums[i])
      rightSum += nums[i]
      
      # If heap size exceeds 'n', remove the smallest element
      # This ensures minHeap always contains the 'n' largest elements encountered so far
      if len(minHeap) == n + 1:
        rightSum -= heapq.heappop(minHeap) # Subtract the popped smallest value
      
      # When minHeap has exactly 'n' elements, rightSum is the sum of these 'n' largest elements.
      # At this point, `i` is the starting index of the right partition.
      # The left partition would end at `i - 1`.
      if len(minHeap) == n:
        # The total array is divided into three parts:
        # 1. Left 'n' elements: sum is minLeftSum[i - 1]
        # 2. Middle 'n' elements: nums[i-n ... i-1] (these are not explicitly summed, but implicitly excluded)
        # 3. Right 'n' elements: sum is rightSum
        # We want to minimize (left_sum - right_sum).
        ans = min(ans, minLeftSum[i - 1] - rightSum)

    return ans

def get_list_of_integers_input(prompt: str) -> List[int]:
    while True:
        try:
            input_str = input(prompt)
            elements = [int(x) for x in input_str.split()]
            if not elements:
                print("List cannot be empty. Please enter at least one integer.")
            elif len(elements) % 3 != 0:
                print("The number of elements in the list must be a multiple of 3.")
            else:
                return elements
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    sol = Solution()
    
    nums_val = get_list_of_integers_input("Enter numbers for the array (e.g., '3 1 2 4 5 6'): ")

    result = sol.minimumDifference(nums_val)
    print(f"The minimum difference is: {result}")