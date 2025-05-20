from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        d = [0] * (len(nums) + 1)
        for l, r in queries:
            d[l] += 1
            d[r + 1] -= 1
        for i in range(len(nums)):
            s += d[i]
            if nums[i] > s:
                return False
        
        s = 0
        for i in range(len(nums)):
            s += d[i] # Current total decrement applied to nums[i]
            if nums[i] != s: # If nums[i] is not exactly equal to the total decrements
                return False
        if s != 0:
            return False

        return True


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        d = [0] * (len(nums) + 1)
        for l, r in queries:
            d[l] += 1
            d[r + 1] -= 1

        s = 0
        for i in range(len(nums)):
            s += d[i]
            if nums[i] != s:
                return False
    
        if s != 0:
            return False

        return True

def get_list_of_ints(prompt: str) -> List[int]:
    while True:
        try:
            input_str = input(prompt)
            return [int(x.strip()) for x in input_str.split(',') if x.strip()]
        except ValueError:
            print("Invalid input. Please enter comma-separated integers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

def get_list_of_list_of_ints(prompt: str) -> List[List[int]]:
    result = []
    print(prompt)
    while True:
        try:
            query_str = input("Enter a query (e.g., '0,2') or 'done' to finish: ")
            if query_str.lower() == 'done':
                break
            parts = [int(x.strip()) for x in query_str.split(',') if x.strip()]
            if len(parts) != 2:
                print("Invalid query format. Please enter two comma-separated integers (l,r).")
                continue
            result.append(parts)
        except ValueError:
            print("Invalid input. Please enter comma-separated integers for the query.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")
    return result

if __name__ == "__main__":
    solution_instance = Solution()

    print("--- Check if Array Can Become All Zeros ---")

    nums_input = get_list_of_ints("Enter the initial array elements (e.g., 1,2,3): ")
    
    if not nums_input:
        print("The initial array cannot be empty.")
    else:
        queries_input = get_list_of_list_of_ints("Now enter the queries. Each query is a range [l,r].")

        result = solution_instance.isZeroArray(nums_input, queries_input)

        if result:
            print("\nResult: True. The array can be reduced to all zeros.")
        else:
            print("\nResult: False. The array cannot be reduced to all zeros.")