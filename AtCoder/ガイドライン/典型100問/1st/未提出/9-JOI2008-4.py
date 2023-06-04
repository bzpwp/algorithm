import numpy as np

m = int(input())
lsm = []
for i in range(m):
    lsm.append(list(map(int,input().split())))
n = int(input())
lsn = []
for j in range(n):
    lsn.append(list(map(int,input().split())))

lsm = np.array(lsm)
lsnnp = np.array(lsn)

point = lsm[0]

# print(lsm)
# print(lsn)


for l in lsn:
    # print([l-point]*m)
    lsnnew = np.array([l-point]*m)+lsm
    x = 0
    for k in lsnnew:
        if list(k) in lsn:
            # print(k)
            # print(lsn)
            x += 1
    if x == m:
        # print("----")
        print(*(l-point))
        # exit()
