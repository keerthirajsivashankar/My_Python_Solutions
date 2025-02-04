n = int(input("Enter the number : "))
n = list(str(n))
n = n[::-1]
n = int("".join(n))
print(f"The reversed number is : {n}")