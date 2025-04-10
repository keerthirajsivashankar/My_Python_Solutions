from functools import cache

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def count(num_str: str) -> int:
            n = len(s)
            m = len(num_str)

            @cache
            def dfs(index: int, tight: bool) -> int:
                if index == m:
                    return 1

                upper = int(num_str[index]) if tight else limit
                ans = 0

                for digit in range(upper + 1):
                    if m - index >= n:
                        sub = num_str[index : index + n]
                        powerful = True
                        for i in range(n):
                            if int(sub[i]) != int(s[i]):
                                powerful = False
                                break
                        if powerful:
                            ans += dfs(index + 1, tight and (digit == upper))
                    else:
                        ans += dfs(index + 1, tight and (digit == upper))
                return ans

            return dfs(0, True)

        def is_powerful(num: int, s: str) -> bool:
            num_str = str(num)
            if len(num_str) < len(s):
                return False
            return num_str[len(num_str) - len(s):] == s

        ans = 0
        for num in range(start, finish + 1):
            if num <= limit and is_powerful(num, s):
                ans += 1
        return ans

# Example Usage (for testing):
if __name__ == "__main__":
    sol = Solution()
    start1 = 1
    finish1 = 60
    limit1 = 6
    s1 = "5"
    print(f"Number of powerful integers between {start1} and {finish1} with limit {limit1} and suffix {s1}: {sol.numberOfPowerfulInt(start1, finish1, limit1, s1)}")

    start2 = 10
    finish2 = 200
    limit2 = 100
    s2 = "19"
    print(f"Number of powerful integers between {start2} and {finish2} with limit {limit2} and suffix {s2}: {sol.numberOfPowerfulInt(start2, finish2, limit2, s2)}")

    start3 = 1
    finish3 = 1000
    limit3 = 1000
    s3 = "00"
    print(f"Number of powerful integers between {start3} and {finish3} with limit {limit3} and suffix {s3}: {sol.numberOfPowerfulInt(start3, finish3, limit3, s3)}")

    start4 = 1
    finish4 = 100
    limit4 = 50
    s4 = "0"
    print(f"Number of powerful integers between {start4} and {finish4} with limit {limit4} and suffix {s4}: {sol.numberOfPowerfulInt(start4, finish4, limit4, s4)}")