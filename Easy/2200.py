from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        key_list = []
        sol = set()

        for i in range(n):
            if nums[i] == key:
                key_list.append(i)

        for i in range(n):
            for j in key_list:
                if abs(i - j) <= k:
                    sol.add(i)

        return sorted(list(sol))

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

def get_integer_input(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    sol = Solution()
    
    nums_val = get_list_of_integers_input("Enter numbers for the array (e.g., '2 2 2 2 2'): ")
    key_val = get_integer_input("Enter the key value: ")
    k_val = get_integer_input("Enter the integer k: ")

    result = sol.findKDistantIndices(nums_val, key_val, k_val)
    print(f"The k-distant indices are: {result}")