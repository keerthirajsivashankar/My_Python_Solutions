l = list(map(int,input("Enter the list : ").split()))
n = len(l)
for i in range(n):
    if l[i] == -1:
        l[i] = 0
ts = (n*(n+1)) / 2
cs = sum(l)
print(int(ts-cs))