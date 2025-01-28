list1 = list(map(int,input("Pls enter the numbers of the list with spaces : ").split()))
m = list1[0]
for i in range(len(list1)):
    if list1[i] > m:
        m = list1[i]
print(f"The Largets element of the list is : {m}")