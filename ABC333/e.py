n = int(input())
events = [list(map(int,input().split())) for _ in range(n)]
draw = []

from collections import defaultdict
dd = defaultdict(int)
for i in range(n):
    t,x = events[-1-i]
    if t == 2:
        dd[x] += 1
    elif t == 1:
        if dd[x]:
            draw.append(1)
            dd[x] -= 1
        else:
            draw.append(0)
draw.reverse()
dd2 = defaultdict(int)
ind = 0
k = 0
have = 0
for t,x in events:
    if t == 1:
        if draw[ind]:
            dd2[x] += 1
            ind += 1
            have += 1
            k = max(k,have)
        else:
            ind += 1
    elif t == 2:
        if dd2[x]:
            dd2[x] -= 1
            have -= 1
        else:
            print(-1)
            exit()
print(k)
print(*draw)

# for i in dd.values():
#     if i != 0:
#         print(-1)
#         exit()
# print(sum(draw))
# print(*draw)