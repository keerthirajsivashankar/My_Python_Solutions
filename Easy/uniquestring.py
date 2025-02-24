def uniquestring(s):
    se = set()
    seen = []
    for c in s:
        if c not in se:
            se.add(c)
            seen.append(c)
    return "".join(seen)
s = input("Enter the stirng : ")
print("The solution is : ",uniquestring(s))