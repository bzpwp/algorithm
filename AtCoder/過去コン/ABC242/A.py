a,b,c,x = map(int, input().split())

if x <= a:
    print(1)
elif x>=a+1 and x<=b:
    print(c/(b-a))
else:
    print(0)