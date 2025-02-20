s = input("Enter the string : ")
stack = []
for c in s:
    stack.append(c)
rs = ""
while stack:
    t = stack.pop()
    rs = rs + t
print(rs)