def min_zero_array(nums: list[int], queries: list[list[int]]) -> int:
    """
    Calculates the minimum number of queries needed to make the 'nums' array non-negative.

    Args:
        nums: A list of integers.
        queries: A list of queries, where each query is a list [l, r, val].

    Returns:
        The minimum number of queries needed, or -1 if it's impossible.
    """
    line = [0] * (len(nums) + 1)
    decrement = 0
    k = 0

    for i, num in enumerate(nums):
        while decrement + line[i] < num:
            if k == len(queries):
                return -1
            l, r, val = queries[k]
            k += 1
            if r < i:
                continue
            line[max(l, i)] += val
            line[r + 1] -= val
        decrement += line[i]

    return k

# Driver Code
if __name__ == "__main__":
    # Example usage:
    nums = [1, 3, 2, 5]
    queries = [[0, 2, 2], [1, 3, 3], [2, 3, 1]]

    result = min_zero_array(nums, queries)
    print(f"Minimum queries needed: {result}")

    # Example 2
    nums2 = [5,2,4,1]
    queries2 = [[0,1,3],[2,3,2],[1,3,1]]
    result2 = min_zero_array(nums2, queries2)
    print(f"Minimum queries needed: {result2}")

    #Example 3
    nums3 = [5,2,4,1]
    queries3 = [[0,1,3],[2,3,2]]
    result3 = min_zero_array(nums3, queries3)
    print(f"Minimum queries needed: {result3}")

    #Example 4
    nums4 = [10, 15, 20]
    queries4 = [[0, 1, 5], [1, 2, 10]]
    result4 = min_zero_array(nums4,queries4)
    print(f"Minimum queries needed: {result4}")

    #Example 5
    nums5 = [10, 15, 20]
    queries5 = [[0, 1, 5]]
    result5 = min_zero_array(nums5,queries5)
    print(f"Minimum queries needed: {result5}")

    #Example 6, impossible case.
    nums6 = [10, 15, 20]
    queries6 = []
    result6 = min_zero_array(nums6,queries6)
    print(f"Minimum queries needed: {result6}")