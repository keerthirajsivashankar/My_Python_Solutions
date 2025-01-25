n = int(input("Enter the number : "))
if n <= 9 :
    s = n
else:
    s = 1 + ((n-1)%9)
print(s)