class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        seen = set()
        for i, num in reversed(list(enumerate(nums))):
            if num in seen:
                return (i + 1 + 2) // 3
            seen.add(num)
        return 0

if __name__ == "__main__":
    try:
        input_str = input("Enter a list of numbers separated by spaces: ")
        nums_str_list = input_str.split()
        nums = [int(num_str) for num_str in nums_str_list]

        solution = Solution()
        result = solution.minimumOperations(nums)
        print(f"Minimum operations: {result}")

    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")
    except Exception as e:
        print(f"An error occurred: {e}")