n,x = map(int,input().split())

ans = 0
for i in range(1,n-1):
    for j in range(i+1,n):
        if x-i-j > j and x-i-j <= n:
            ans += 1

print(ans)