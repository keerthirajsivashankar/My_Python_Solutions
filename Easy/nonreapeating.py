from collections import Counter 
def nonerepeating(s):
    count = Counter(s)
    for k,v in count.items():
        if v == 1 :
            return k
            break
    else:
        return None
s = input("Enter the string : ")
print(nonerepeating(s))