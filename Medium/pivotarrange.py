def pivot(arr,t):
    f = []
    p = []
    e = []
    for n in arr:
        if n < t :
            f.append(n)
        elif n == t :
            p.append(n)
        else:
            e.append(n)
    return f + p + e
#driver code
arr = list(map(int,input("Enter the list : ").split()))
t = int(input("Enter the pivot : "))
print(pivot(arr,t))