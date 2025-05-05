class Solution:
    def numTilings(self, n: int) -> int:
        """
        Calculates the number of ways to tile a 2 x n board with dominoes and trominoes.

        Args:
            n: The length of the board.

        Returns:
            The number of ways to tile the board modulo 10^9 + 7.
        """
        MOD = 1_000_000_007
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[n]

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    n1 = 3
    print(f"Number of tilings for n={n1}: {sol.numTilings(n1)}")

    n2 = 1
    print(f"Number of tilings for n={n2}: {sol.numTilings(n2)}")

    n3 = 2
    print(f"Number of tilings for n={n3}: {sol.numTilings(n3)}")

    n4 = 4
    print(f"Number of tilings for n={n4}: {sol.numTilings(n4)}")

    n5 = 5
    print(f"Number of tilings for n={n5}: {sol.numTilings(n5)}")