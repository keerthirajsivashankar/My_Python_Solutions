# cook your dish here
def work(b1,b2,b3):
    ref = b1+b2+b3
    
    if ref < 2:
        return "Water filling time"
        
    else:
        return "Not now"
        
t = int(input())
while t:
    t -= 1 
    b1,b2,b3 = map(int,input().split())
    print(work(b1,b2,b3))