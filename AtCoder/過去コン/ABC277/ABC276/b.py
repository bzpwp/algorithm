n,m = map(int,input().split())
ls = [[]for _ in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    ls[a-1].append(b)
    ls[b-1].append(a)
for l in ls:
    l.sort()
    print(len(l),*l)