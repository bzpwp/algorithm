n, m, q = map(int,input().split())
lsuv = []
for i in range(m):
    lsuv.append(list(map,input().split()))
lsc = list(map(int,input().split()))
for i in range(q):
    w = input()
    if w[0]=="1":
        print(lsc[int(w[3])])
