list1 = list(map(int,input("Enter the list elements with space betwwen : ").split()))
if len(list1) == 0 or len(list1) == 1:
    print("No largest Second Number")
else:
    n = len(list1)
    m = list1[0]
    for i in list1:
        if i > m:
            m = i 
    list1 = [i for i in list1 if m!=i]
    if len(list1) == 0 :
        print("NO second largest number")
    else:
        m1 = list1[0]
        for i in list1:
            if i > m1 :
                m1 = i
        print(m1)