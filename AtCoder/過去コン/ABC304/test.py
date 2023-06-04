
from sys import stdin

# input = stdin.readline
# setrecursionlimit(10**6)
# @lru_cache

N,D=map(int,input().split())
X=[]
Y=[]
for i in range(N):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)
class UnionFind():
    def __init__(self, n):
            self.n = n
            self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def roots(self):
            return [i for i, x in enumerate(self.parents) if x < 0]
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    def group_count(self):
            return len(self.roots())
    def size(self, x):
            return -self.parents[self.find(x)]
uf=UnionFind(N)
for i in range(N):
    for j in range(i+1,N):
        if (X[i]-X[j])**2+(Y[i]-Y[j])**2<=D**2:
            uf.union(i,j)

for i in range(N):
    if uf.same(i,0):
        print("Yes")
    else:
        print("No")