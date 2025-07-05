from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        hp = Counter(arr)

        for key, freq in hp.items():
            if key == freq:
                res = max(res, key)

        return res

def get_list_of_integers_input(prompt: str) -> List[int]:
    while True:
        try:
            input_str = input(prompt)
            elements = [int(x) for x in input_str.split()]
            return elements
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    sol = Solution()
    
    arr_val = get_list_of_integers_input("Enter numbers for the array (e.g., '2 2 3 4'): ")

    result = sol.findLucky(arr_val)
    print(f"The largest lucky number is: {result}")