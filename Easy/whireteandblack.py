class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        countB = 0
        maxCountB = 0
        for i , block in enumerate(blocks):
            if block == 'B':
                countB += 1
            if i >= k and blocks[i - k] == 'B':
                countB -= 1
            maxCountB = max(countB,maxCountB)
        return k - maxCountB  
s = Solution()
Blocks = input("Enter the string of W & B : ")
K = int(input('Enter the Consecutive value : '))
print(s.minimumRecolors(Blocks,K))