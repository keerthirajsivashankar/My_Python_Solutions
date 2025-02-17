n = int(input("Enter the number : "))
if n <= 1:
    print("Enter a valid number greater than 1 .")
else:
    c = 0
    for i in range(1,n+1):
        s = str(i)
        c = c + s.count('2')
print(c)