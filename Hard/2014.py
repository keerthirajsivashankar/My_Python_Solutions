from collections import deque
from typing import List

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def isK(sub: str, t: str, k: int) -> bool:
            count = i = 0
            for ch in t:
                if i < len(sub) and ch == sub[i]:
                    i += 1
                    if i == len(sub):
                        i = 0
                        count += 1
                        if count == k:
                            return True
            return False

        res = ""
        q = deque([""])
        while q:
            curr = q.popleft()
            for ch in map(chr, range(ord('a'), ord('z') + 1)):
                nxt = curr + ch
                if isK(nxt, s, k):
                    res = nxt
                    q.append(nxt)
        return res

def get_string_input(prompt: str) -> str:
    while True:
        s_val = input(prompt)
        if s_val.isalpha() and s_val.islower():
            return s_val
        else:
            print("Invalid input. Please enter a string containing only lowercase English letters.")

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
    
    s_val = get_string_input("Enter the string s: ")
    k_val = get_integer_input("Enter the integer k: ")

    result = sol.longestSubsequenceRepeatedK(s_val, k_val)
    print(f"The longest subsequence repeated k times is: '{result}'")