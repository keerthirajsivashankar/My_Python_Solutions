from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """
        Checks if an array contains three consecutive odd numbers.

        Args:
            arr: A list of integers.

        Returns:
            True if the array contains three consecutive odd numbers, False otherwise.
        """
        n = len(arr)

        for i in range(1, n - 1):
            if arr[i] % 2 == 1 and arr[i - 1] % 2 == 1 and arr[i + 1] % 2 == 1:
                return True

        return False

def get_array_from_input() -> List[int]:
    """
    Gets an array of integers from user input.  Handles potential errors
    """
    while True:
        try:
            input_str = input("Enter the integers for the array, separated by spaces: ")
            nums = [int(x.strip()) for x in input_str.split()]
            if not nums:
                print("Array cannot be empty. Please enter at least one number.")
                continue
            return nums
        except ValueError:
            print("Invalid input. Please enter integers only, separated by spaces.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try entering the array again.")

def main():
    """
    Main function to run the program.
    """
    solution = Solution()
    arr = get_array_from_input()
    result = solution.threeConsecutiveOdds(arr)

    if result:
        print("The array contains three consecutive odd numbers.")
    else:
        print("The array does not contain three consecutive odd numbers.")

if __name__ == "__main__":
    main()
