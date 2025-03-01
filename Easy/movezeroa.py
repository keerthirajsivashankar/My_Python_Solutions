def move_zeros(arr):
    i = 0  # Pointer to place the next non-zero element
    
    for j in range(len(arr)):
        if arr[j] != 0:  # If non-zero element found
            arr[i], arr[j] = arr[j], arr[i]  # Swap
            i += 1  # Move non-zero pointer forward

    return arr  # Array modified in-place

# Driver Code
arr = list(map(int, input("Enter the list: ").split()))
print("Modified array:", move_zeros(arr))
