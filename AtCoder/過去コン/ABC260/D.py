n,k = map(int, input().split())
ls = list(map(int, input().split()))
import bisect

lsa = [-1]*n
lsb = []
lsc = []

num = 1
for i in ls:
    if lsc == []:
        lsc.append(i)
        lsb.append([i])
        num += 1
    else:
        index = bisect.bisect(lsc,i)
        if index == len(lsc):
            lsc.append(i)
            lsb.append([i])
            num += 1
        else:
            d = lsc[index]
            lsb[index].append(d)
            if len (lsb[index])>= k:
                lsa[index]=num

for i in lsa:
    print(i)