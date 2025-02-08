from collections import Counter
def majority(l):
    counter = Counter(l)
    for key,value in counter.items():
        if value > len(l) // 2:
            return key
    return -1
l = list(map(int,input("Enter the list : ").split()))
print(majority(l))