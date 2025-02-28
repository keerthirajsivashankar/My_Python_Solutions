def target_sum(arr,t):
    arr = list(set(arr))
    if len(arr) < 2:
        return []
    i = 0
    j = len(arr) - 1
    res = []
    while i < j:
        s = arr[i] + arr[j]
        if s == t:
            res.append([arr[i],arr[j]])
            i += 1
            j -= 1
        elif s > t :
            j -= 1
        elif s < t :
            i += 1
    if res:
        return res
    else:
        return []
#driver code 
arr = list(map(int,input("Enter the List : ").split()))
t = int(input("Enter the target value : "))
print(target_sum(arr,t))