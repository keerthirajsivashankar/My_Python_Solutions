def climbingstairs(n):
    
    if n == 1 :
        return 1
    elif n == 2 :
        return 2
    else :
        a = 1
        b = 1
        for i in range(2,n+1):
            c = a+b 
            a = b
            b = c
        return c
#driver code 

n = int(input("Enter the stair case count : "))
print("The number of ways we can climb the staris : ",climbingstairs(n))
        