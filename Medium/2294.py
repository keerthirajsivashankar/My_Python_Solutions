from typing import List

class Solution:
  def partitionArray(self, nums: List[int], k: int) -> int:
    nums.sort()

    ans = 1
    mn = nums[0]

    for i in range(1, len(nums)):
      if mn + k < nums[i]:
        ans += 1
        mn = nums[i]

    return ans

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
    
    nums_val = get_list_of_integers_input("Enter numbers separated by spaces (e.g., '3 6 1 2 5'): ")
    k_val = get_integer_input("Enter the value of k: ")

    result = sol.partitionArray(nums_val, k_val)
    print(f"The minimum number of partitions is: {result}")