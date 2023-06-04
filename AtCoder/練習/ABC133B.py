n, d = map(int,input().split())
ls = []
for i in range(n):
    ls.append(list(map(int,input().split())))

dis = []
total = 0
for a in range(n):
    for b in range(a+1,n):
        dis = [(ls[a][c]-ls[b][c])**2 for c in range(d)]
        if pow(sum(dis),0.5) == int(pow(sum(dis),0.5)):
            total += 1
print(total)

