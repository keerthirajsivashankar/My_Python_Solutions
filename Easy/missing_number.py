l = list(map(int,input("Enter the list : ").split()))
n = len(l)
cs = sum(l)
asum = (n*(n+1)) / 2
print(int(asum - cs))