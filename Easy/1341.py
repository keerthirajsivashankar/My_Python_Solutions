from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff = -1
        mn = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > mn:
                diff = max(diff, nums[i] - mn)
            if nums[i] < mn:
                mn = nums[i]
        
        return diff

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
    
    nums_val = get_list_of_integers_input("Enter numbers separated by spaces (e.g., '7 1 5 4'): ")

    result = sol.maximumDifference(nums_val)
    print(f"The maximum difference is: {result}")