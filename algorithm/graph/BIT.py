'''
# BITのソースコード
'''

class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
        
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

'''
# バブルソートの交換回数
'''

# 入力
n = int(input())
a = list(map(int,input().split()))

# BITのソースコード
class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
        
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

BIT = BinaryIndexedTree(n)
ans = 0
for j in range(n):
    ans += j - BIT.sum(a[j])
    BIT.add(a[j], 1)
print(ans)