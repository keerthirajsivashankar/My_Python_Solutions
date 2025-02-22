def isrepeating(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        else:
            seen.add(num)
    
arr = list(map(int,input("Enter the list with space : ").split()))
print(isrepeating(arr))
