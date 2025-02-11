def length_of_longest_substring(s):
    char_set = set()  # To store unique characters
    left = 0  # Left pointer for the sliding window
    max_length = 0  # Store the maximum length found

    for right in range(len(s)):  # Right pointer expands the window
        while s[right] in char_set:  # If duplicate found, shrink window
            char_set.remove(s[left])
            left += 1  # Move left pointer

        char_set.add(s[right])  # Add current char to the set
        max_length = max(max_length, right - left + 1)  # Update max length

    return max_length  # Return the maximum substring length

# Input handling
s = input("Enter the string: ")
print("Length of longest substring without repeating characters:", length_of_longest_substring(s))
