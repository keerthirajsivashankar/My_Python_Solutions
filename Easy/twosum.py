nums = list(map(int, input("Enter the elements: ").split()))
k = int(input("Target element: "))
h = {}

for i, num in enumerate(nums):
    d = k - num
    if d in h:  
        print([h[d], i])  
        break
    h[num] = i  
