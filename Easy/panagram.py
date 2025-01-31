s = input("Enter the string : ")
ns = set()
for c in s.lower():
    if "a" <= c <= "z":
        ns.add(c)
if len(ns) == 26 :
    print("Yes it is pangram")
else:
    print("It is not a pangram")