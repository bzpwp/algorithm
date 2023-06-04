n,k = map(int, input().split())
lsa = list(map(int, input().split()))
lsb = list(map(int, input().split()))
import sys
sys.setrecursionlimit(1000000000)

def dfs(c,x):
    if x == n-1:
        print("Yes")
        sys.exit()
    elif abs(c-lsa[x+1]) <= k:
        dfs(lsa[x+1],x+1)
    elif abs(c-lsb[x+1]) <= k:
        dfs(lsb[x+1],x+1)

dfs(lsa[0],0)
dfs(lsb[0],0)
print("No")