def minOperations(grid, x):
    # Flatten and sort the grid
    arr = sorted([a for row in grid for a in row])

    # Check if it's possible to make all elements equal
    if any((a - arr[0]) % x for a in arr):
        return -1
    
    # Find the median
    median = arr[len(arr) // 2]
    
    # Calculate the minimum operations
    ans = sum(abs(a - median) // x for a in arr)
    
    return ans

# Input the grid dimensions
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

# Input the grid
print("Enter the elements row-wise:")
grid = [list(map(int, input().split())) for _ in range(m)]

# Input the value of x
x = int(input("Enter the value of x: "))

# Calculate and print the result
result = minOperations(grid, x)
print("Minimum operations required:", result)
