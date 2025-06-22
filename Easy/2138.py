from typing import List

class Solution:
  def divideString(self, s: str, k: int, fill: str) -> List[str]:
    return [
        s[i:] + fill * (i + k - len(s)) if i + k > len(s)
        else s[i:i + k]
        for i in range(0, len(s), k)
    ]

def get_string_input(prompt: str) -> str:
    return input(prompt)

def get_integer_input(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_fill_char_input(prompt: str) -> str:
    while True:
        char = input(prompt)
        if len(char) == 1:
            return char
        else:
            print("Please enter a single character for fill.")

if __name__ == "__main__":
    sol = Solution()
    
    s_val = get_string_input("Enter the string: ")
    k_val = get_integer_input("Enter the value of k (group size): ")
    fill_val = get_fill_char_input("Enter the fill character (single character): ")

    result = sol.divideString(s_val, k_val, fill_val)
    print(f"The divided string is: {result}")