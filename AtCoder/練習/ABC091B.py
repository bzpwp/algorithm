n = int(input())
lsn = [input() for s in range(n)]
m = int(input())
lsm = [input() for t in range(m)]

dics = {}
dict = {}
for s in lsn:
    dics[s]=lsn.count(s)
for t in lsm:
    dict[t]=lsm.count(t)

for t in dict:
    if t in dics:
        dics[t]-=dict[t]

if max(list(dics.values()))<0:
    print(0)
else:
    print(max(list(dics.values())))
