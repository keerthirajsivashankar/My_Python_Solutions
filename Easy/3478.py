class Solution:
    def maxSum(self, nums):
        mx = max(nums)
        if mx <= 0 :
            return mx 
        seen = set()
        ans = 0
        for num in nums:
            if num < 0 or num in seen :
                continue     
            seen.add(num)
            ans += num 

        return ans 
    
s = Solution()
print(s.maxSum(nums = [1,2,3,4,5]))
