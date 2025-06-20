import math

class Solution:
  def maxDistance(self, s: str, k: int) -> int:
    return max(self._flip(s, k, 'NE'), self._flip(s, k, 'NW'),
               self._flip(s, k, 'SE'), self._flip(s, k, 'SW'))

  def _flip(self, s: str, k: int, direction: str) -> int:
    res = 0
    pos = 0
    opposite = 0

    for c in s:
      if c in direction:
        pos += 1
      else:
        pos -= 1
        opposite += 1
      res = max(res, pos + 2 * min(k, opposite))

    return res

def get_string_input(prompt: str) -> str:
    while True:
        s_val = input(prompt)
        if all(char in 'NESW' for char in s_val):
            return s_val
        else:
            print("String must contain only 'N', 'E', 'S', 'W' characters (e.g., 'NEESWW').")

def get_integer_input(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    sol = Solution()
    
    s_val = get_string_input("Enter the path string (e.g., 'NEESWW'): ")
    k_val = get_integer_input("Enter the integer k: ")

    result = sol.maxDistance(s_val, k_val)
    print(f"The maximum distance is: {result}")