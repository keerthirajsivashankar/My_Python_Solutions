class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        # Step 1: Use Sieve of Eratosthenes to find all primes up to 'right'
        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
            for i in range(2, int(n ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return [i for i in range(n + 1) if is_prime[i]]

        # Step 2: Get primes within the given range
        primes = sieve(right)
        primes = [p for p in primes if p >= left]

        # Step 3: Find the closest pair
        if len(primes) < 2:
            return [-1, -1]  # No pair exists

        min_diff = float('inf')
        res = [-1, -1]

        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] < min_diff:
                min_diff = primes[i + 1] - primes[i]
                res = [primes[i], primes[i + 1]]

        return res
s = Solution()
n , m = map(int,input("Enter the numbers : ").split())
print(s.closestPrimes(n,m))