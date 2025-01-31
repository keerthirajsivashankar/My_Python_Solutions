from collections import Counter
s = input("Enter the string : ")
count = Counter(s)
for i,c in enumerate(s):
    if count[c] == 1:
        print(f"The unique value within the string is {c} ad the position is {i}")
        break
    else:
        print("Thier is no uniques values.")