# cook your dish here
def isinrange(nums,num,k):
    l = num - k 
    u = num + k 
    
    for n in nums:
        if n <= u and n >= l and n != num :
            return True 
            
    return False
    
def func(nums,k,n):
    count = 0
    
    for num in nums:
        if isinrange(nums,num,k):
            count += 1
        
    return count 

#driver code 

n , k = map(int,input().split())
nums = list(map(int,input().split()))
print(func(nums,k,n))