x,y,n  = map(int, input().split())

if 3*x > y :
    print((y*(n//3))+(x*(n%3)))
else:
    print(x*n)