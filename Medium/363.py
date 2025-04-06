def largest_divisible_subset(nums: list[int]) -> list[int]:
    """
    Finds the largest subset of a given set of distinct positive integers,
    such that every pair of elements (Si, Sj) in this subset satisfies
    either Si % Sj == 0 or Sj % Si == 0.

    Args:
        nums: A list of distinct positive integers.

    Returns:
        The largest divisible subset. If multiple such subsets exist, return any of them.
    """
    n = len(nums)
    if n == 0:
        return []

    ans = []
    count = [1] * n
    prev_index = [-1] * n
    max_count = 0
    index = -1

    nums.sort()

    for i, num in enumerate(nums):
        for j in reversed(range(i)):
            if num % nums[j] == 0 and count[i] < count[j] + 1:
                count[i] = count[j] + 1
                prev_index[i] = j
        if count[i] > max_count:
            max_count = count[i]
            index = i

    while index != -1:
        ans.append(nums[index])
        index = prev_index[index]

    return ans

if __name__ == "__main__":
    nums1 = [1, 2, 3]
    result1 = largest_divisible_subset(nums1)
    print(f"Largest divisible subset for {nums1}: {result1}")

    nums2 = [1, 2, 4, 8]
    result2 = largest_divisible_subset(nums2)
    print(f"Largest divisible subset for {nums2}: {result2}")

    nums3 = [4, 8, 10, 240]
    result3 = largest_divisible_subset(nums3)
    print(f"Largest divisible subset for {nums3}: {result3}")

    nums4 = [2, 3, 4, 6, 8]
    result4 = largest_divisible_subset(nums4)
    print(f"Largest divisible subset for {nums4}: {result4}")

    nums5 = [1]
    result5 = largest_divisible_subset(nums5)
    print(f"Largest divisible subset for {nums5}: {result5}")

    nums6 = []
    result6 = largest_divisible_subset(nums6)
    print(f"Largest divisible subset for {nums6}: {result6}")

    nums7 = [3, 4, 16, 8]
    result7 = largest_divisible_subset(nums7)
    print(f"Largest divisible subset for {nums7}: {result7}")