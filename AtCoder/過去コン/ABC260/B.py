n,x,y,z = map(int, input().split())

lsa = list(map(int, input().split()))
lsb = list(map(int, input().split()))

answer = []
for i in range(x):
    c = lsa.index(max(lsa))
    answer.append(c+1)
    lsa[c]=-10*18
    lsb[c]=-10*18
for j in range(y):
    c = lsb.index(max(lsb))
    answer.append(c+1)
    lsa[c]=-10*18
    lsb[c]=-10*18

lsc = []

for k in range(n):
    lsc.append(lsa[k]+lsb[k])

for i in range(z):
    c = lsc.index(max(lsc))
    answer.append(c+1)
    lsc[c]=-10*18

answer.sort()
for i in answer:
    print(i)