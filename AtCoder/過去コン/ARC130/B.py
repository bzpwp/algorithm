h,w,c,q = map(int, input().split())
ls = []
for i in range(q):
    ls.append(list(map(int,input().split())))
ls.reverse()
x = []
for i in range(h):
    for j in range(w):
        for k in range(len(ls)):
            if (ls[k][0]==1 and ls[k][1]==i) or (ls[k][0]==2 and ls[k][1]==j):
                x.append(ls[k][2])
                break
y = [x.count(l+1) for l in range(c)]
print(*y)