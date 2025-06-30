from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0

        for key, vals in count.items():
            dest = key + 1
            if dest in count:
                res = max(res, vals + count[dest])

        return res

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
    
    nums_val = get_list_of_integers_input("Enter numbers separated by spaces (e.g., '1 3 2 2 5 2 3 7'): ")

    result = sol.findLHS(nums_val)
    print(f"The length of the longest harmonious subsequence is: {result}")