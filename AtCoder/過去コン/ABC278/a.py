n,k = map(int,input().split())
ls = list(map(int,input().split()))

ls = ls[k:]+[0]*(min(k,n))
print(*ls)