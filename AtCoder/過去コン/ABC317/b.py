n = int(input())
ls = list(map(int,input().split()))

ls.sort()
for i in range(n-1):
    if ls[i+1]-ls[i]==2:
        print(ls[i]+1)