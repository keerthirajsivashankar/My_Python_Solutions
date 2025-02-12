from collections import Counter
l = list(map(int,input().split()))
c = 0
count = Counter(l)
for key,frq in count.items():
    if frq == 1:
        print(key)
        c = c +1 
if c == 0 :
    print(-1)
l = list(map(int, input().split()))
result = 0

for num in l:
    result ^= num  # XOR cancels out duplicate numbers

print(result)
