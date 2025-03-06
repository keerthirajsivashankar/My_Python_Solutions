def missing_num(grid):
    count = [1] + [0] * len(grid)**2
    for row in grid:
        for num in row:
            count[num] += 1
    return [count.index(2),count.index(0)]
#drive code 
n = int(input("Enter the size of the matrix : "))
grid = []
for i in range(n):
    row = list(map(int,input("Enter the row : ").split()))
    grid.append(row)
print(missing_num(grid))