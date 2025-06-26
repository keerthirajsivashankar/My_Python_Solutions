class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res = cur = 0
        for c in reversed(s):
            if c == '0':
                res += 1
            else:
                if cur + (1 << res) <= k:
                    cur += 1 << res
                    res += 1
        return res

def get_binary_string_input(prompt: str) -> str:
    while True:
        s_val = input(prompt)
        if all(char in '01' for char in s_val):
            return s_val
        else:
            print("Invalid input. Please enter a binary string (containing only '0's and '1's).")

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
    
    s_val = get_binary_string_input("Enter the binary string s: ")
    k_val = get_integer_input("Enter the integer k: ")

    result = sol.longestSubsequence(s_val, k_val)
    print(f"The length of the longest subsequence is: {result}")