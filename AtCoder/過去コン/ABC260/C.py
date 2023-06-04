n,x,y = map(int, input().split())
ls = [0,1]
if n == 1:
    print(0)
else:
    for i in range(n-1):
        b = ls[1]*y+ls[0]
        a = b*x+ls[0]
        ls[0]=a
        ls[1]=b
    print(ls[0])