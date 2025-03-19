def min_operations(nums: list[int]) -> int:
    """
    Calculates the minimum number of operations to make all elements non-zero.

    Args:
        nums: A list of integers (0 or 1).

    Returns:
        The minimum number of operations, or -1 if it's impossible.
    """
    ans = 0
    for i, x in enumerate(nums):
        if x == 0:
            if i + 2 >= len(nums):
                return -1
            nums[i + 1] ^= 1
            nums[i + 2] ^= 1
            ans += 1
    return ans

if __name__ == "__main__":
    nums1 = [0, 1, 0, 1]
    result1 = min_operations(nums1)
    print(f"Minimum operations for {nums1}: {result1}")

    nums2 = [1, 0, 0, 1]
    result2 = min_operations(nums2)
    print(f"Minimum operations for {nums2}: {result2}")

    nums3 = [0, 0, 0, 0]
    result3 = min_operations(nums3)
    print(f"Minimum operations for {nums3}: {result3}")

    nums4 = [1, 1, 1, 1]
    result4 = min_operations(nums4)
    print(f"Minimum operations for {nums4}: {result4}")

    nums5 = [0, 1]
    result5 = min_operations(nums5)
    print(f"Minimum operations for {nums5}: {result5}")

    nums6 = [1, 0]
    result6 = min_operations(nums6)
    print(f"Minimum operations for {nums6}: {result6}")

    nums7 = [0]
    result7 = min_operations(nums7)
    print(f"Minimum operations for {nums7}: {result7}")

    nums8 = [0,0,1,0,1,0,0]
    result8 = min_operations(nums8)
    print(f"Minimum operations for {nums8}: {result8}")