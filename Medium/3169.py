def countDays(days: int, meetings: list[list[int]]) -> int:
    freeDays = 0
    prevEnd = 0

    # Sort the meetings based on start days
    for start, end in sorted(meetings):
        if start > prevEnd:
            freeDays += start - prevEnd - 1
        prevEnd = max(prevEnd, end)

    return freeDays + max(0, days - prevEnd)

# Taking inputs from the terminal
days = int(input("Enter the total number of days: "))
n = int(input("Enter the number of meetings: "))

meetings = []
for i in range(n):
    start, end = map(int, input(f"Enter the start and end day of meeting {i+1} (space-separated): ").split())
    meetings.append([start, end])

# Output result
print("Number of free days:", countDays(days, meetings))
