l1 = list(map(int,input("Enter the elements of first list : ").split()))
l2 = list(map(int,input("Enter the elements of second list : ").split()))
res = []
n = len(l1)
m = len(l2)
if n < m:
    for e in l1:
        if e in l2:
            res.append(e)
else:
    for e in l2:
        if e in l1:
            res.append(e)
print(res)
#another approach
from collections import Counter

l1 = list(map(int, input("Enter the elements of first list: ").split()))
l2 = list(map(int, input("Enter the elements of second list: ").split()))

count1 = Counter(l1)  # Count occurrences in l1
count2 = Counter(l2)  # Count occurrences in l2

res = []
for num in count1:
    if num in count2:
        res.extend([num] * min(count1[num], count2[num]))  # Take min occurrences

print(res)
