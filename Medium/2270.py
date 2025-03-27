import collections

def minimumIndex(nums):
    # Create two counters to keep track of frequencies
    count1 = collections.Counter()
    count2 = collections.Counter(nums)

    # Iterate through the array
    for i, num in enumerate(nums):
        count1[num] += 1
        count2[num] -= 1

        # Check the conditions for the dominant number
        if count1[num] * 2 > i + 1 and count2[num] * 2 > len(nums) - i - 1:
            return i

    return -1

# Input
nums = list(map(int, input("Enter the list of numbers: ").split()))

# Function call
result = minimumIndex(nums)

# Output the result
print("Minimum index where the dominant number exists:", result)
