def countMerged(intervals):
    count = 0
    prev_end = -1
    for start, end in sorted(intervals):
        if start > prev_end:
            count += 1
            prev_end = end
        else:
            prev_end = max(prev_end, end)
    return count

def checkValidCuts(n, rectangles):
    x_intervals = [(rect[0], rect[2]) for rect in rectangles]
    y_intervals = [(rect[1], rect[3]) for rect in rectangles]

    return max(countMerged(x_intervals), countMerged(y_intervals)) >= 3

# Input
n = int(input("Enter the number of rectangles: "))
rectangles = []

print("Enter rectangles in the format x1 y1 x2 y2:")

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    rectangles.append([x1, y1, x2, y2])

# Check if grid can be cut into sections
if checkValidCuts(n, rectangles):
    print("Yes, the grid can be cut into sections.")
else:
    print("No, the grid cannot be cut into sections.")
