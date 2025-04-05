import functools
import operator

def subset_xor_sum(nums: list[int]) -> int:
    """
    Calculates the sum of XOR sums of all subsets of a list of integers.

    Args:
        nums: A list of integers.

    Returns:
        The sum of XOR sums of all subsets.
    """
    if not nums:
        return 0
    return functools.reduce(operator.or_, nums) << (len(nums) - 1)

if __name__ == "__main__":
    nums1 = [1, 3]
    result1 = subset_xor_sum(nums1)
    print(f"Subset XOR sum for {nums1}: {result1}")

    nums2 = [5, 1, 6]
    result2 = subset_xor_sum(nums2)
    print(f"Subset XOR sum for {nums2}: {result2}")

    nums3 = [3, 4, 5, 6, 7, 8]
    result3 = subset_xor_sum(nums3)
    print(f"Subset XOR sum for {nums3}: {result3}")

    nums4 = [0]
    result4 = subset_xor_sum(nums4)
    print(f"Subset XOR sum for {nums4}: {result4}")

    nums5 = [1, 1, 1]
    result5 = subset_xor_sum(nums5)
    print(f"Subset XOR sum for {nums5}: {result5}")

    nums6 = []
    result6 = subset_xor_sum(nums6)
    print(f"Subset XOR sum for {nums6}: {result6}")