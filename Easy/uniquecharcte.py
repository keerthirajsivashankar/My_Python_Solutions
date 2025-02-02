from collections import Counter

s = input("Enter the string: ")
s = Counter(s)
c = 0

for key, value in s.items():  # Iterate over key-value pairs
    if value == 1:  # Find the first unique character
        print(key)  # Print the first unique character
        c = 1
        break

if c == 0:
    print(None)  # If no unique character is found, print 0
