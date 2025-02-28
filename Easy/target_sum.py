def target_sum(arr , t):
    if len(arr) < 2 :
        return []
    i = 0
    j = len(arr) - 1
    while i < j:
        s = arr[i] + arr[j]
        if s == t:
            return [ i + 1 , j + 1 ]
        elif s > t :
            j -= 1
        elif s < t :
            i += 1
    return []
#driver code 
arr = list(map(int,input("Enter the List : ").split()))
t = int(input("Enter the target value : "))
print(target_sum(arr,t))