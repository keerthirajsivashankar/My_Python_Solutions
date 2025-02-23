def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Sort the array
    strs.sort()
    
    first = strs[0]
    last = strs[-1]
    i = 0
    
    # Compare characters of first and last string
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    
    return first[:i]

# Example test cases
print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
print(longestCommonPrefix(["apple", "ape", "april"]))     # Output: "ap"
