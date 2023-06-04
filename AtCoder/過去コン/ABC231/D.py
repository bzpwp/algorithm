n,m = map(int,input().split())
ls = []
for i in range(m):
    ls.append(list(input().split()))
ls.sort()

ls1 = []
for a in range(m):
    ls1.append(ls[a][0])
    ls1.appned(ls[a][1])
