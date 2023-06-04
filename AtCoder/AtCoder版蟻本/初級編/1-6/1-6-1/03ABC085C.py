n,y = map(int,input().split())
a = y//10000
a = min(n,a)
for i in range(0,a+1):
    for j in range(0,n-i+1):
        if 10000*i+5000*j+1000*(n-i-j)==y:
            print(i,j,n-i-j)
            exit()
print(-1,-1,-1)