from collections import Counter
a = list(map(int,input("Enter the list : ").split(",")))
u = []
r = []
n = len(a)
for num in a:
    if num>9:
        while num > 9:
            t = num % 10
            num = num // 10
            u.append(t)
        if num < 9:
            u.append(num)
    else:
        u.append(num)
print(u)
count = Counter(u)
m = 0
for key,val in count.items():
    if val > m :
        m = val
for key,val in count.items():
    if val >= m:
        r.append(key)
print(sorted(r))
