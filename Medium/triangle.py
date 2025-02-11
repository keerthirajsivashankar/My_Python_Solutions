a = list(map(int,input("Enter the list : ").split()))
r = []
n = len(a)
for i in range(n-2):
    j = i + 1
    k = i + 2
    if a[i] + a[j] == a[k] or a[i] + a[k] == a[j] or a[j] + a[k] == a[i]:
        r.append(0)
    elif a[i] + a[j] > a[k] or a[i] + a[k] > a[j] or a[j] + a[k] > a[i] :
        r.append(1)
print(r)