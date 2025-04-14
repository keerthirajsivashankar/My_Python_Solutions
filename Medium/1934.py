import itertools

class Solution:
  def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
    return sum(abs(arr[i] - arr[j]) <= a and
               abs(arr[j] - arr[k]) <= b and
               abs(arr[i] - arr[k]) <= c
               for i, j, k in itertools.combinations(range(len(arr)), 3))

if __name__ == "__main__":
  solution = Solution()
  while True:
    try:
      arr_str = input("Enter the array of integers (comma-separated): ")
      arr_input = [int(x.strip()) for x in arr_str.split(',')]
      a_input = int(input("Enter the value for 'a': "))
      b_input = int(input("Enter the value for 'b': "))
      c_input = int(input("Enter the value for 'c': "))

      result = solution.countGoodTriplets(arr_input, a_input, b_input, c_input)
      print(f"The number of good triplets is: {result}")
      break  # Exit the loop after successful input and calculation

    except ValueError:
      print("Invalid input. Please enter integers separated by commas for the array and integer values for a, b, and c.")
    except KeyboardInterrupt:
      print("\nExiting the program.")
      break