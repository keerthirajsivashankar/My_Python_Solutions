def count_less_or_equal(matrix, x):
    cnt = 0
    c = len(matrix[0]) - 1
    for row in matrix:
        while c >= 0 and row[c] > x:
            c -= 1
        cnt += (c + 1)
    return cnt

def kth_smallest(matrix, k):
    left, right = matrix[0][0], matrix[-1][-1]
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if count_less_or_equal(matrix, mid) >= k:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

n, k = map(int, input().split())
flowers = [list(map(int, input().split())) for _ in range(n)]
print(kth_smallest(flowers, k))