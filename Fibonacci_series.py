f = [0, 1]
n = int(input("Enter the length of the Fibonacci series: "))

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("The last number in the Fibonacci series:", f[0])
else:
    for i in range(2, n):
        t = f[i-2] + f[i-1]
        f.append(t)  
    print("The last number in the Fibonacci series:", f[-1])
