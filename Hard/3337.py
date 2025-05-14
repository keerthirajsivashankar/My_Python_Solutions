from typing import List

class Solution:
    # Similar to 3335. Total Characters in String After Transformations I
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        """
        Calculates the length of the string after applying 't' transformations,
        where the transformation rules are defined by 'nums'.

        Args:
            s: The initial string.
            t: The number of transformations to apply.
            nums: A list of integers, where nums[i] represents the number of steps
                  to shift character 'a' + i.  'z' shifts to 'ab' and so on.

        Returns:
            The length of the string after 't' transformations, modulo 10^9 + 7.
        """
        MOD = 1_000_000_007

        def matrixMult(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
            """Returns A * B (matrix multiplication)."""
            sz = len(A)
            C = [[0] * sz for _ in range(sz)]
            for i in range(sz):
                for j in range(sz):
                    for k in range(sz):
                        C[i][j] += A[i][k] * B[k][j]
                        C[i][j] %= MOD
            return C

        def matrixPow(M: List[List[int]], n: int) -> List[List[int]]:
            """Returns M^n (matrix exponentiation)."""
            if n == 0:
                return [[1 if i == j else 0  # identity matrix
                        for j in range(len(M))]
                        for i in range(len(M))]
            if n % 2 == 1:
                return matrixMult(M, matrixPow(M, n - 1))
            return matrixPow(matrixMult(M, M), n // 2)

        # T[i][j] := the number of ways to transform ('a' + i) to ('a' + j) in one step
        T = self._getTransformationMatrix(nums)
        # T^t represents the number of ways to transform ('a' + i) to ('a' + j) in t steps
        poweredT = matrixPow(T, t)

        count = [0] * 26  # Count of each character in the initial string
        lengths = [0] * 26 # Length contribution of each character after t transformations

        for c in s:
            count[ord(c) - ord('a')] += 1

        for i in range(26):
            for j in range(26):
                # poweredT[i][j] gives the number of characters that 'a' + i becomes after t steps
                # For every character 'a' + i in the original string (count[i]), it contributes
                # count[i] * poweredT[i][j] to the final count of character 'a' + j
                lengths[j] += count[i] * poweredT[i][j]
                lengths[j] %= MOD

        return sum(lengths) % MOD

    def _getTransformationMatrix(self, nums: List[int]) -> List[List[int]]:
        """
        Constructs the transformation matrix T based on the given 'nums'.

        T[i][j] represents the number of ways to transform character 'a' + i to
        character 'a' + j in one step.
        """
        T = [[0] * 26 for _ in range(26)]
        for i, steps in enumerate(nums):
            for step in range(1, steps + 1):
                T[i][(i + step) % 26] += 1
        return T

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    s1 = "abc"
    t1 = 1
    nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    print(f"Length after {t1} transformations of '{s1}' with nums {nums1}: {sol.lengthAfterTransformations(s1, t1, nums1)}")

    s2 = "z"
    t2 = 1
    nums2 = [1] * 26
    print(f"Length after {t2} transformations of '{s2}' with nums {nums2}: {sol.lengthAfterTransformations(s2, t2, nums2)}")

    s3 = "a"
    t3 = 26
    nums3 = [1] * 26
    print(f"Length after {t3} transformations of '{s3}' with nums {nums3}: {sol.lengthAfterTransformations(s3, t3, nums3)}")

    s4 = "az"
    t4 = 1
    nums4 = [1, 2] * 13
    print(f"Length after {t4} transformations of '{s4}' with nums {nums4}: {sol.lengthAfterTransformations(s4, t4, nums4)}")

    s5 = "zz"
    t5 = 2
    nums5 = [2] * 26
    print(f"Length after {t5} transformations of '{s5}' with nums {nums5}: {sol.lengthAfterTransformations(s5, t5, nums5)}")

    s6 = "abc"
    t6 = 2
    nums6 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
    print(f"Length after {t6} transformations of '{s6}' with nums {nums6}: {sol.lengthAfterTransformations(s6, t6, nums6)}")
