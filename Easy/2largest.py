arr = list(map(int,input("Enter the list : ").split()))
arr = sorted(list(set(arr)))
print(arr[-2])