from collections import Counter

s = input("Enter the string: ")
count = Counter(s)

for i, c in enumerate(s):
    if count[c] == 1:
        print(f"The unique value within the string is '{c}' at the position {i}")
        break
else:  # This runs only if the loop completes without finding a unique character
    print("There are no unique values.")
