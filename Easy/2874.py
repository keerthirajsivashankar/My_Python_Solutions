def maximum_triplet_value(nums: list[int]) -> int:
    """
    Calculates the maximum triplet value (nums[i] - nums[j]) * nums[k].

    Args:
        nums: A list of integers.

    Returns:
        The maximum triplet value.
    """
    ans = 0
    max_diff = 0  # max(nums[i] - nums[j])
    max_num = 0   # max(nums[i])

    for num in nums:
        ans = max(ans, max_diff * num)    # num := nums[k]
        max_diff = max(max_diff, max_num - num)  # num := nums[j]
        max_num = max(max_num, num)      # num := nums[i]

    return ans

if __name__ == "__main__":
    nums1 = [12, 6, 1, 2, 7]
    result1 = maximum_triplet_value(nums1)
    print(f"Maximum triplet value for {nums1}: {result1}")

    nums2 = [1, 10, 3, 4, 19]
    result2 = maximum_triplet_value(nums2)
    print(f"Maximum triplet value for {nums2}: {result2}")

    nums3 = [1,2,3]
    result3 = maximum_triplet_value(nums3)
    print(f"Maximum triplet value for {nums3}: {result3}")

    nums4 = [10,9,8,7,6]
    result4 = maximum_triplet_value(nums4)
    print(f"Maximum triplet value for {nums4}: {result4}")

    nums5 = [1]
    result5 = maximum_triplet_value(nums5)
    print(f"Maximum triplet value for {nums5}: {result5}")

    nums6 = []
    result6 = maximum_triplet_value(nums6)
    print(f"Maximum triplet value for {nums6}: {result6}")