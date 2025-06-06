def func(n):
    res = ''
    while n > 0 :
        res = str(n%2) + res 
        n //= 2
    return res 
def func1(n):
    s = func(n)
    n = len(s)
    i = 0 
    j = n-1
    while i < j :
        if s[i] != s[j]:
            return False 
        i+=1
        j -=1
    return True 
    
n = int(input("Enter the number : "))
print(func(n))
print(func1(n))