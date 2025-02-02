from collections import Counter

def canFormPalindrome(s: str) -> bool:
    char_count = Counter(s)  # Create a frequency map of characters
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    
    return odd_count <= 1  # A string can be a palindrome if at most 1 odd count exists

s = input("Enter the string : ")
print(canFormPalindrome(s))  # True
