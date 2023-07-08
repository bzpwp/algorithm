n = int(input())
ls = list(map(int,input().split()))
s = input()

M_ind = []
E_ind = []
X_ind = []

for i in range(n):
    if s[i] == "M":
        M_ind.append(i)
    elif s[i] == "E":
        E_ind.append(i)
    elif s[i] == "X":
        X_ind.append(i)

import bisect
def mex(a,b,c):
    for i in range(4):
        if i not in set([a,b,c]):
            return i
A = 0
for j in E_ind:
    indr = bisect.bisect_right(M_ind,j)
    indl = bisect.bisect_right(X_ind,j)
