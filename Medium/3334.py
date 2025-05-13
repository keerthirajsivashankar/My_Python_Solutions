class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        """
        Calculates the length of the string after applying 't' transformations.

        Each transformation shifts characters as follows:
        'a' -> 'b', 'b' -> 'c', ..., 'y' -> 'z', 'z' -> 'ab' (length increases).

        Args:
            s: The initial string.
            t: The number of transformations to apply.

        Returns:
            The length of the string after 't' transformations, modulo 10^9 + 7.
        """
        MOD = 1_000_000_007
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        for _ in range(t):
            new_count = [0] * 26
            # 'a' -> 'b', 'b' -> 'c', ..., 'y' -> 'z'
            for i in range(25):
                new_count[i + 1] = count[i]
            # 'z' -> 'ab'
            new_count[0] = count[25]
            new_count[1] = (new_count[1] + count[25]) % MOD
            count = new_count

        return sum(count) % MOD

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    s1 = "abc"
    t1 = 1
    print(f"Length after {t1} transformations of '{s1}': {sol.lengthAfterTransformations(s1, t1)}")  # Output: 3

    s2 = "z"
    t2 = 1
    print(f"Length after {t2} transformations of '{s2}': {sol.lengthAfterTransformations(s2, t2)}")  # Output: 2

    s3 = "a"
    t3 = 26
    print(f"Length after {t3} transformations of '{s3}': {sol.lengthAfterTransformations(s3, t3)}") # Output: 2

    s4 = "az"
    t4 = 1
    print(f"Length after {t4} transformations of '{s4}': {sol.lengthAfterTransformations(s4, t4)}")

    s5 = "zz"
    t5 = 2
    print(f"Length after {t5} transformations of '{s5}': {sol.lengthAfterTransformations(s5, t5)}")