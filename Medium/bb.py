import bisect as bs

T = int(input())
while T:
    T -= 1
    N, Q = map(int, input().split())
    L = list(map(int, input().split()))
    L.sort()
    sum=[0] * N
    for j in range(1, N):
        sum[j] = sum[j - 1] + L[j]
    for i in range(Q):
        K = int(input())
        pos = bs.bisect_left(L, K)
        l = 0 
        r = pos
        while l < r:
            m = (l + r) // 2
            need = K * (pos -m ) - (sum[pos - 1] - sum[m - 1])
            if(need <= m):
                r = m
            else:
                l = m + 1
        print(N - r)        