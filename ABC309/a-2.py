a,b = map(int,input().split())
if a + 1 == b:
    if a%3 == 0:
        print("No")
    else:
        print("Yes")
else:
    print("No")