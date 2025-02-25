def findpeak(arr):
    for i in range(1,len(arr)-1):
        if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
            return i
    return None
arr = list(map(int,input("Enter the list : ").split()))
print(findpeak(arr))