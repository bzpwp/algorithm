n,m = map(int,input().split())

ls = []
for i in range(n):
    ls.append(list(map(int,input().split())))

# print(ls)

import itertools

lsn = list(range(m))
# print(lsn)

lsp = itertools.permutations(lsn,2)

answer = 0
for l in lsp:
    # print(l)
    ans = 0
    x = l[0]
    y = l[1]
    for i in range(n):
        ans += max(ls[i][x],ls[i][y])
    # print(ans)
    answer = max(answer,ans)

print(answer)