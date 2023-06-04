class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

n,h = map(int,input().split())

from collections import defaultdict

td = defaultdict(int)
dt = defaultdict(int)

for i in range(n):
    t,d = map(int,input().split())
    td[t] = max(td[t],d)
    dt[d] = max(dt[d],t)

bit = Bit(h)
 