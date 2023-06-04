a,b,c,x,y = map(int,input().split())


ans = 10**18
for i in range(x+1):
    for j in range(y+1):
        ans = min(i*a+j*b+max(x-i,y-j)*2*c,ans)
        if ans == 8200:
            print(i,j)

print(ans)