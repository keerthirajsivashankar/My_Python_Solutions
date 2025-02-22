from collections import Counter 
def isrepeating(arr):
    count = Counter(arr)
    for k,f in count.items():
        if f > 1:
            return k
    
arr = list(map(int,input("Enter the list with space : ").split()))
print(isrepeating(arr))
