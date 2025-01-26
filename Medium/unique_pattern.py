n = int(input("Enter the number of rows : "))
s = 1
for i in range(1,n+1):
    s = i 
    for j in range(i):
        print(s , end = " ")
        s = s + n - j - 1
    print(end="\n")
        