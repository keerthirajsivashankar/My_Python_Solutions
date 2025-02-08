l = list(map(int,input("Enter the list : ").split()))
l = list(set(l))
if len(l) < 2:
    print(-1)
else:
    m = max(l)
    l.remove(m)
    m = max(l)
    print(m)