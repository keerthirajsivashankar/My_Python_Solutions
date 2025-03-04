def sum_3(n):
    while n > 0:
        if n % 3 == 0:
            n //= 3
        elif n % 3 == 1:
            n = n -1 
        else:
            return False
    return True
#driver code
n = int(input("Enter the Number : "))
print(sum_3(n))