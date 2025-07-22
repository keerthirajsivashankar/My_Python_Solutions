from typing import List
import collections

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = 0
        current_sum = 0
        max_sum = 0
        
        for right in range(len(nums)):
            while nums[right] in seen:
                current_sum -= nums[left]
                seen.remove(nums[left])
                left += 1
            current_sum += nums[right]
            seen.add(nums[right])
            max_sum = max(max_sum, current_sum)
        
        return max_sum

def get_list_of_integers_input(prompt: str) -> List[int]:
    while True:
        try:
            input_str = input(prompt)
            elements = [int(x) for x in input_str.split()]
            if not elements:
                print("List cannot be empty. Please enter at least one integer.")
            else:
                return elements
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    sol = Solution()
    
    nums_val = get_list_of_integers_input("Enter numbers for the array separated by spaces (e.g., '4 2 4 5 6'): ")

    result = sol.maximumUniqueSubarray(nums_val)
    print(f"The maximum unique subarray sum is: {result}")