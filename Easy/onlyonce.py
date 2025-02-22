"""#approach 1 

def onlyonce(arr):
    seen = []
    for num in arr:
        if num in seen:
            seen.remove(num)
        else:
            seen.append(num)
    if len(seen) == 1:
        return seen[0]
    elif len(seen) > 1:
        return seen[0]
    else:
        return "No unique elements"
arr = list(map(int,input("Enter the list : ").split()))
print(onlyonce(arr))
#approach 2
from collections import Counter
def onlyonce2(arr):
    count = Counter(arr)
    for k,f in count.items():
        if f == 1:
            print(k)
            return
    else:
        print("Not found ")
 """
def onlyonce1(arr):
    res = 0 
    for num in arr:
        res = res ^ num
    if res == 0:
        print("No unique elements")
    else:
        print(res)
arr = list(map(int,input("Enter the list : ").split()))
onlyonce1(arr)
