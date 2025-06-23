class Solution:
  def kMirror(self, k: int, n: int) -> int:
    ans = 0
    A = ['0']

    def nextKMirror(current_k_mirror_digits: list[str]) -> list[str]:
      # Iterate from the middle towards the end to find the digit to increment
      # This handles both odd and even length palindromes gracefully
      # For A = ['1', '2', '1'], len(A)//2 = 1. i starts at 1.
      # For A = ['1', '2', '2', '1'], len(A)//2 = 2. i starts at 2.
      for i in range(len(current_k_mirror_digits) // 2, len(current_k_mirror_digits)):
        # Convert the digit character back to an integer, increment it
        nextNum = int(current_k_mirror_digits[i]) + 1
        
        # If the incremented digit is still less than k (the base)
        if nextNum < k:
          # Update the digit at current position and its mirror position
          current_k_mirror_digits[i] = str(nextNum)
          current_k_mirror_digits[~i] = str(nextNum) # ~i is a clever way to get the mirror index
          
          # Reset all digits between the current position and the center to '0'
          # This ensures we find the lexicographically smallest next palindrome
          for j in range(len(current_k_mirror_digits) // 2, i):
            current_k_mirror_digits[j] = '0'
            current_k_mirror_digits[~j] = '0'
          return current_k_mirror_digits
      
      # If we couldn't increment any digit (e.g., all are k-1, like ['1', '1'] for k=2),
      # it means we need to expand the length of the palindrome.
      # This creates a new palindrome of length len(A) + 2, like '10...01'
      return ['1'] + ['0'] * (len(current_k_mirror_digits) - 1) + ['1']

    # Loop n times to find the first n k-mirror numbers
    for _ in range(n):
      while True:
        # Get the next lexicographical palindrome in base k
        A = nextKMirror(A)
        
        # Convert this base-k number to base-10
        # int(''.join(A), k) converts the list of digit strings to a string,
        # then converts that string to an integer using base k.
        num = int(''.join(A), k)
        
        # Check if the base-10 representation is also a palindrome
        if str(num)[::-1] == str(num):
          break # Found a k-mirror number, exit inner loop
      ans += num # Add the k-mirror number to the total sum

    return ans

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
    
    k_val = get_integer_input("Enter the base k (2 <= k <= 9): ")
    n_val = get_integer_input("Enter the count n (number of k-mirror numbers to sum): ")

    if not (2 <= k_val <= 9):
        print("Error: k must be between 2 and 9 inclusive.")
    else:
        result = sol.kMirror(k_val, n_val)
        print(f"The sum of the first {n_val} k-mirror numbers in base {k_val} is: {result}")