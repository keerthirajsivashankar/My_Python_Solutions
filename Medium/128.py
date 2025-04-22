def missign_positive(nums):
    n = len(nums)
    curr_sum = sum(nums)
    ac_sum = n * (n+1) // 2
    ans = ac_sum - curr_sum
    return ans 
nums = list(map(int,input("Enter the list : ").split()))
print("The missing number : ",missign_positive(nums))