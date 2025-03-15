import bisect

def min_capability(nums: list[int], k: int) -> int:
    def num_stolen_houses(capacity: int) -> int:
        stolen_houses = 0
        i = 0
        while i < len(nums):
            if nums[i] <= capacity:
                stolen_houses += 1
                i += 1
            i += 1
        return stolen_houses

    return bisect.bisect_left(range(max(nums) + 1), k, key=num_stolen_houses)

if __name__ == "__main__":
    nums1 = [2, 3, 5, 9]
    k1 = 2
    result1 = min_capability(nums1, k1)
    print(f"Minimum capability for {nums1}, {k1}: {result1}")

    nums2 = [2, 7, 9, 3, 1]
    k2 = 2
    result2 = min_capability(nums2, k2)
    print(f"Minimum capability for {nums2}, {k2}: {result2}")

    nums3 = [1,2,5,3,9,10,12,6]
    k3 = 4
    result3 = min_capability(nums3,k3)
    print(f"Minimum capability for {nums3}, {k3}: {result3}")

    nums4 = [1,2,5,3,9,10,12,6]
    k4 = 1
    result4 = min_capability(nums4,k4)
    print(f"Minimum capability for {nums4}, {k4}: {result4}")

    nums5 = [1,2,5,3,9,10,12,6]
    k5 = 8
    result5 = min_capability(nums5,k5)
    print(f"Minimum capability for {nums5}, {k5}: {result5}")

    nums6 = [2,2,2,2]
    k6 = 2
    result6 = min_capability(nums6,k6)
    print(f"Minimum capability for {nums6}, {k6}: {result6}")