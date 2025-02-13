def find_smallest_missing(nums):
    n = len(nums)

    # Step 1: Place each number in its correct index (if possible)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]  # Swap to correct position

    # Step 2: Find the first missing positive
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1  # First missing positive number

    return n + 1  # If all numbers are present, return the next number

# Input handling
n = int(input("Enter the number of elements: "))
nums = list(map(int, input("Enter the list: ").split()))

print("Smallest missing positive number:", find_smallest_missing(nums))
