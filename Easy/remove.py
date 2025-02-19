s = input("Enter the enter : ")
v = ['a','e','i','o','u']
ns = ''
for char in s:
    if char.lower() not in v:
        ns = ns + char
print(ns)