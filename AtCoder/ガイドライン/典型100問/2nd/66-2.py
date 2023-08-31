import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left #bisect_left(list, value)
from heapq import *
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
def pri(x): print('\n'.join(map(str, x)))


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

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

class Cell:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def calc_dist(c1, c2):
    return ((c1.x - c2.x)**2 + (c1.y - c2.y)**2 + (c1.z - c2.z)**2)**(1/2)

ans = []
while True:
    n = int(input())
    if n == 0:
        break
    cells = []
    for _ in range(n):
        x, y, z, r = list(map(float, input().split()))
        c = Cell(x, y, z)
        cells.append((r, c))

    # 各辺を繋いでいく
    G = []
    for i in range(n-1):
        for j in range(i+1, n):
            r1, c1 = cells[i]
            r2, c2 = cells[j]
            dist = calc_dist(c1, c2)
            if dist > r1 + r2:
                G.append((dist-(r1+r2), (i, j)))
            else:
                G.append((0, (i, j)))

    G.sort()
    for i in G:
        print(i)
    res = 0
    uf = UnionFind(n)
    for i in range(len(G)):
        w = G[i][0]
        s = G[i][1][0]
        t = G[i][1][1]

        if uf.same(s, t):
            continue
        res += w
        uf.union(s, t)
    ans.append(res)

for res in ans:
    print('{:.3f}'.format(res))