import string

class Solution:
  def kthCharacter(self, k: int) -> str:
    return string.ascii_lowercase[(k - 1).bit_count()]

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

if __name__ == "__main__":
    sol = Solution()
    
    k_val = get_integer_input("Enter the integer k: ")

    result = sol.kthCharacter(k_val)
    print(f"The {k_val}-th character is: {result}")