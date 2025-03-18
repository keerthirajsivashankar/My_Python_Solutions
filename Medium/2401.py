def longest_nice_subarray(nums: list[int]) -> int:
    """
    Finds the length of the longest nice subarray.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest nice subarray.
    """
    ans = 0
    used = 0

    l = 0
    for r, num in enumerate(nums):
        while used & num:
            used ^= nums[l]
            l += 1
        used |= num
        ans = max(ans, r - l + 1)

    return ans

if __name__ == "__main__":
    nums1 = [1, 3, 8, 48, 10]
    result1 = longest_nice_subarray(nums1)
    print(f"Longest nice subarray for {nums1}: {result1}")

    nums2 = [3, 1, 5, 11, 13]
    result2 = longest_nice_subarray(nums2)
    print(f"Longest nice subarray for {nums2}: {result2}")

    nums3 = [1,2,4,8,16]
    result3 = longest_nice_subarray(nums3)
    print(f"Longest nice subarray for {nums3}: {result3}")

    nums4 = [1,2,3,4,5,6,7,8,9,10]
    result4 = longest_nice_subarray(nums4)
    print(f"Longest nice subarray for {nums4}: {result4}")

    nums5 = [1]
    result5 = longest_nice_subarray(nums5)
    print(f"Longest nice subarray for {nums5}: {result5}")

    nums6 = []
    result6 = longest_nice_subarray(nums6)
    print(f"Longest nice subarray for {nums6}: {result6}")