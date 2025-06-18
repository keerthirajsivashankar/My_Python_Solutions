from typing import List

class Solution:
  def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
    ans = []

    nums.sort()

    for i in range(2, len(nums), 3):
      if nums[i] - nums[i - 2] > k:
        return []
      ans.append([nums[i - 2], nums[i - 1], nums[i]])

    return ans

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
    
    nums_val = get_list_of_integers_input("Enter numbers separated by spaces (e.g., '1 3 4 8 7 9 3 5 1'): ")
    k_val = get_integer_input("Enter the value of k: ")

    result = sol.divideArray(nums_val, k_val)
    print(f"The divided array is: {result}")