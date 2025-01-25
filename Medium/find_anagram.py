from collections import Counter

def find_anagrams(s, p):
    # Initialize the result list
    result = []
    
    # Length of the input strings
    n, m = len(s), len(p)
    
    # If length of p is greater than length of s, no anagrams possible
    if n < m:
        return result
    
    # Create a frequency counter for string p
    p_count = Counter(p)
    
    # Create a frequency counter for the first window in string s
    window_count = Counter(s[:m])
    
    # Check the first window
    if window_count == p_count:
        result.append(0)
    
    # Now slide the window across string s
    for i in range(1, n - m + 1):
        # Remove the character going out of the window
        window_count[s[i - 1]] -= 1
        if window_count[s[i - 1]] == 0:
            del window_count[s[i - 1]]  # Remove it from the counter if it reaches 0
        
        # Add the new character coming into the window
        window_count[s[i + m - 1]] += 1
        
        # Compare the current window's frequency map with that of p
        if window_count == p_count:
            result.append(i)
    
    return result

# Example usage:
s = "cbaebabacd"
p = "abc"
print(find_anagrams(s, p))  # Output: [0, 6]
