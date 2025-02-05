n = int(input("Enter the number of elements : "))
l = []
for i in range(n):
    ele = int(input("Enter the element to add in list : "))
    l.append(ele)
for i in range(n):
    if l[i] < 0:
        l[i] = 0 
tsum = (n*(n+1))/2
asum = sum(l)
m = int(tsum - asum) 
print(f"The missing number : {m}")
n = int(input("Enter the number of elements: "))
l = []
for i in range(n):
    ele = int(input("Enter the element to add in list: "))
    l.append(ele)

# Step 1: Use a set to track existing numbers
num_set = set(l)

# Step 2: Find the first missing positive number
missing = 1
while missing in num_set:
    missing += 1

print(f"The missing number: {missing}")
