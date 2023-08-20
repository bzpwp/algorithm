
# N: 頂点数
# E = [(cost, v, w), ...]
#   G上の全ての辺(v, w)とそのcostを含むlist



N = int(input())

info = [list(map(float,input().split())) for _  in range(N)]

E = []
import math
for i in range(N-1):
    for j in range(i+1, N):
        dist = math.sqrt((info[i][0]-info[j][0])**2+(info[i][1]-info[j][1])**2+(info[i][2]-info[j][2])**2)
        r = info[i][3] + info[j][3]
        if r < dist:
            E.append((dist-r, i, j))
            E.append((dist-r, j, i))

print(E)
# Union-Findを使うことで頂点間の連結判定を行う
*p, = range(N)
def root(x):
    if x == p[x]:
        return x
    p[x] = y = root(p[x])
    return y
 
def unite(x, y):
    px = root(x); py = root(y)
    if px == py:
        return 0
    if px < py:
        p[py] = px
    else:
        p[px] = py
    return 1
 
E.sort()
ans = 0
for c, v, w in E:
    if unite(v, w):
        ans += c

print(ans)
# ansが最小全域木の解