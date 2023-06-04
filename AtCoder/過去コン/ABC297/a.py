n,d = map(int, input().split())
ls = list(map(int,input().split()))
for i in range(n-1):
    if ls[i+1]-ls[i] <= d:
        print(ls[i+1])
        exit()

print(-1)