from collections import Counter 
def freq(s):
    count = Counter(s)
    m = 0
    for v in count.values():
        if v > m:
            m = v
    for k,v in count.items():
        if v == m:
            return k
s = input("Enter the string : ")
print(freq(s))