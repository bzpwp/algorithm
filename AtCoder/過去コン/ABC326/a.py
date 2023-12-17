a,b = map(int,input().split())
if a >= b:
    if a - b <=3:
        print("Yes")
    else:
        print("No")
else:
    if b - a <=2:
        print("Yes")
    else:
        print("No")