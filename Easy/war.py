# cook your dish here
def war(n,nums):
    even = 0
    odd = 0
    
    for num in nums :
        if num % 2 == 0 :
            even += 1
        else :
            odd += 1
            
    if even > odd :
        return "READY FOR BATTLE"
    else :
        return "NOT READY"
        
#driver code 

n = int(input())
nums = list(map(int,input().split()))
print(war(n , nums))