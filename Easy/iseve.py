def iseven(n):
    if n == 0:
        return True
    elif n < 0:
        return "enter a valid number "
    elif n // 2 == n / 2:
        return True
    else :
        return False


n = int(input("enter the number : "))
print(iseven(n))