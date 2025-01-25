a,b,c = map(int,input("Enter the three numbers leaving space inbetween : ").split())

if (a == b or a == c or b == c ):
    print("Enter Three Different Numbers")
else:
    if(a>b and a>c):
        print(f"{a} is the greatest of three")
    elif(b>a and b>c):
        print(f"{b} is the greatest of three")
    else:
        print(f"{c} is the greatest of three")