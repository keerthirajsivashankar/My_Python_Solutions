from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        """
        Finds the longest subsequence of 'words' where no two consecutive words
        belong to the same group.

        Args:
            words: A list of strings.
            groups: A list of integers, where groups[i] represents the group of words[i].

        Returns:
            A list of strings representing the longest subsequence.
        """
        # List comprehension to construct the subsequence
        return [words[i] for i, x in enumerate(groups) if i == 0 or x != groups[i - 1]]

def get_list_from_input(prompt, type_converter):
    """
    Gets a list from user input, handling potential errors.

    Args:
        prompt: The prompt to display to the user.
        type_converter: The function to convert the input string to the desired type (e.g., int, str).

    Returns:
        A list of the specified type.
    """
    while True:
        try:
            input_str = input(prompt)
            items = [type_converter(item.strip()) for item in input_str.split(',')]
            return items
        except ValueError:
            print("Invalid input. Please enter comma-separated values of the correct type.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try entering the list again.")

def main():
    """
    Main function to run the program.
    """
    solution = Solution()

    words = get_list_from_input("Enter the words, separated by commas: ", str)
    groups = get_list_from_input("Enter the group numbers, separated by commas: ", int)

    if len(words) != len(groups):
        print("Error: The number of words and group numbers must be the same.")
        return

    result = solution.getLongestSubsequence(words, groups)
    print("Longest subsequence:", result)

if __name__ == "__main__":
    main()

