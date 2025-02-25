def sqrt(n):
    i , j = 1 , n
    while i < j :
        m = (i+j)//2
        if m**2 == n:
            return m
        elif m**2 > n:
            j = m 
        else:
            i = m + 1
    
    return i - 1
n = int(input("Enter the number : "))
print(sqrt(n))