class Solution:
  def clearStars(self, s: str) -> str:
    ans = list(s)
    buckets = [[] for _ in range(26)]

    for i, c in enumerate(s):
      if c == '*':
        ans[i] = ''
        j = next(j for j, bucket in enumerate(buckets) if bucket)
        ans[buckets[j].pop()] = ''
      else:
        buckets[ord(c) - ord('a')].append(i)

    return ''.join(ans)

if __name__ == "__main__":
  user_input_s = input("Enter a string: ")
  solution = Solution()
  result = solution.clearStars(user_input_s)
  print(f"The modified string is: {result}")