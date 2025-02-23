def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0  # Left pointer of the window
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:  
            char_set.remove(s[left])  # Remove leftmost character
            left += 1  # Move the left pointer
            
        char_set.add(s[right])  # Add current character to the set
        max_length = max(max_length, right - left + 1)  # Update max length

    return max_length

# Example Test Cases
s = input("Enter the string: ")
print("Longest Substring Length:", lengthOfLongestSubstring(s))
