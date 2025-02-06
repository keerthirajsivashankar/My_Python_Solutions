s = input("Enter the string: ")
freq = {}

# Step 1: Count frequency of each character
for char in s:
    freq[char] = freq.get(char, 0) + 1

# Step 2: Find first non-repeating character
for i in range(len(s)):
    if freq[s[i]] == 1:
        print(i)
        break
else:
    print(-1)  # If no unique character found
