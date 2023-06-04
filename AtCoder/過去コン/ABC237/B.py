h,w = map(int, input().split())
ls = []
for i in range(h):
    ls.append(list(map(int,input().split())))
x = []
for a in range(w):
    x.append([])
for a in range(h):
    for b in range(w):
        x[b].append(ls[a][b])
for a in range(w):
    print(*x[a])