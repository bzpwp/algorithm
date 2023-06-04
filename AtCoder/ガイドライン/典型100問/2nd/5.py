a,b,c,x,y = map(int,input().split())

A = 10**18

for i in range(x+1):
    z = a*i + c*(x-i)*2 + min(b*max(0,y-(x-i)),c*max(0,y-(x-i))*2)
    # print(z,i,x-i,y-(x-i))
    A = min(A,z)
print(A)
