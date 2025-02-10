def subsets(nums):
    result = [[]]  # Start with the empty subset
    for num in nums:
        result += [curr + [num] for curr in result]
    return result

# Example usage:
input_list = [1, 2, 3]
print("All possible subsets:", subsets(input_list))
