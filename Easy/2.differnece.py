def difference(arr, t):
    if len(arr) < 2:
        return False
    i, j = 0, 1  # Start j from 1 instead of last index
    
    while j < len(arr):
        d = arr[j] - arr[i]
        if d == t:
            return True
        elif d < t:  # Increase j to get a larger difference
            j += 1
        else:  # Increase i to reduce the difference
            i += 1
        if i == j:  # Ensure i and j are not the same
            j += 1
    return False

# Driver Code
arr = list(map(int, input("Enter the list: ").split()))
t = int(input("Enter the difference: "))
print(difference(arr, t))
