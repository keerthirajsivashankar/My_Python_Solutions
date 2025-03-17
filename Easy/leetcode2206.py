import collections

def divide_array(nums: list[int]) -> bool:
    """
    Determines if an array can be divided into pairs of equal elements.

    Args:
        nums: A list of integers.

    Returns:
        True if the array can be divided into pairs, False otherwise.
    """
    counts = collections.Counter(nums)
    return all(count % 2 == 0 for count in counts.values())

if __name__ == "__main__":
    nums1 = [3, 2, 3, 2, 2, 2]
    result1 = divide_array(nums1)
    print(f"Can {nums1} be divided into pairs? {result1}")

    nums2 = [1, 2, 3, 4]
    result2 = divide_array(nums2)
    print(f"Can {nums2} be divided into pairs? {result2}")

    nums3 = [3,3,3,3,4,4,5,5]
    result3 = divide_array(nums3)
    print(f"Can {nums3} be divided into pairs? {result3}")

    nums4 = [3,3,3,3,4,4,5]
    result4 = divide_array(nums4)
    print(f"Can {nums4} be divided into pairs? {result4}")

    nums5 = [2]
    result5 = divide_array(nums5)
    print(f"Can {nums5} be divided into pairs? {result5}")

    nums6 = []
    result6 = divide_array(nums6)
    print(f"Can {nums6} be divided into pairs? {result6}")