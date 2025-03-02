from collections import Counter
def mergeArrays(nums1, nums2):
    cnt = Counter()
    for i, v in nums1 + nums2:
        cnt[i] += v
    return sorted(cnt.items())
arr1 = [[1,2],[2,3],[4,5]]
arr2 = [[1,4],[3,2],[4,1]]
print(mergeArrays(arr1,arr2))
