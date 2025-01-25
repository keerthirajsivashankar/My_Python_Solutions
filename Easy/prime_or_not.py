n = int(input("Enter the number : "))
v = True
if n <= 1 :
    v = False
else:
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            v = False
            break
if v :
    print("The Number is a Prime")
else:
    print("The Number is not a Prime")