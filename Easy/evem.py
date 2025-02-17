arr = list(map(int,input("Enter the numbers : ").split()))
even = []
for num in arr:
    if num % 2 == 0:
        even.append(num)
print(even)