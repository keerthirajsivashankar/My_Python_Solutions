from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        """
        Determines the type of triangle based on the lengths of its sides.

        Args:
            nums: A list of three integers representing the lengths of the sides of a triangle.

        Returns:
            A string representing the type of triangle:
            - "equilateral": All three sides are equal.
            - "isosceles": Two sides are equal.
            - "scalene": No sides are equal.
            - "none": The given side lengths cannot form a triangle.
        """
        nums.sort()  # Sort the sides in non-decreasing order.
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return "isosceles"
        else:
            return "scalene"

def get_triangle_sides() -> List[int]:
    """
    Gets the side lengths of a triangle from the user.  Handles input validation.

    Returns:
        A list of three integers representing the side lengths, or an empty list on error.
    """
    while True:
        try:
            input_str = input("Enter the three side lengths of the triangle, separated by spaces: ")
            sides = [int(s.strip()) for s in input_str.split()]
            if len(sides) != 3:
                print("Invalid input. Please enter exactly three numbers.")
                continue  # Restart the loop
            if any(side <= 0 for side in sides):
                print("Invalid input. Side lengths must be positive.")
                continue
            return sides  # Return the list if input is valid
        except ValueError:
            print("Invalid input. Please enter integers only, separated by spaces.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}") # print the error
            print("Please try entering the side lengths again.")

def main():
    """
    Main function to run the program.
    """
    solution = Solution()
    sides = get_triangle_sides()
    if sides: # check if the sides are valid
        triangle_type = solution.triangleType(sides)
        print(f"The triangle type is: {triangle_type}")

if __name__ == "__main__":
    main()

