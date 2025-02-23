def singleNonDuplicate(nums):
    low, high = 0, len(nums) - 1

    while low < high:
        mid = low + (high - low) // 2

        # Ensure mid is even
        if mid % 2 == 1:
            mid -= 1  # Move mid to even index
        
        if nums[mid] == nums[mid + 1]:  # Unique element is on the right
            low = mid + 2
        else:  # Unique element is on the left or is nums[mid]
            high = mid

    return nums[low]  # The unique element

# Example test cases
nums1 = [1,1,2,2,3,3,4,4,5,6,6,7,7]
nums2 = [2,2,3,3,4,4,8,8,9]

print(singleNonDuplicate(nums1))  # Output: 5
print(singleNonDuplicate(nums2))  # Output: 9
