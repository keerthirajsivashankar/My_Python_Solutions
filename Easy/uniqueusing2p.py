def remove_duplicates(arr):
    if not arr:
        return 0  # Edge case: empty array

    i = 0  # Slow pointer (tracks unique elements)

    for j in range(1, len(arr)):  # Fast pointer (scans the array)
        if arr[j] != arr[i]:  # Found a new unique element
            i += 1
            arr[i] = arr[j]  # Move unique element forward

    return i + 1  # New length of modified array

# Driver Code
arr = list(map(int, input("Enter the sorted list: ").split()))
new_length = remove_duplicates(arr)
print("New length:", new_length)
print("Modified array:", arr[:new_length])  # Display only the unique elements
