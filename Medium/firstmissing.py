def first_missing_positive(nums):
    n = len(nums)
    
    # Step 1: Place each number in its correct position if possible
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]  # Swap
    
    # Step 2: Find the first missing positive number
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    return n + 1  # If all numbers are in place, return the next positive integer

# Example test cases
print(first_missing_positive([3, 4, -1, 1]))  # Output: 2
print(first_missing_positive([1, 2, 0]))      # Output: 3
print(first_missing_positive([7, 8, 9, 11, 12]))  # Output: 1
