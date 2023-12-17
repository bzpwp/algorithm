d = int(input())

ls = []
x = 0
while x**2 <= d:
    ls.append(x**2)
    x += 1

import bisect

A = d
n = len(ls)
for i in ls:
    ind = bisect.bisect_left(ls, d-i)
    if ind == n:
        A = min(A, d-i-ls[-1])
    elif ind == 0:
        print(0)
        exit()
    else:
        A = min(A, i + ls[ind] - d)
        A = min(A, d - i - ls[ind-1])
print(A)
# print(ls)