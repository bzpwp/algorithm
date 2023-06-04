n,m = map(int, input().split())
lsa = list(map(int, input().split()))
lsc = list(map(int, input().split()))

l = [[]]*(m+1)

def dfs(x,y,z):
    if x-1>=0 and y -1 >=0:
        ls[z].append(lsa[x-1]*lsb{y-1})