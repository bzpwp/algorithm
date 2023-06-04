n = int(input())
ls = list((map(int,input().split())))
import bisect
for i in range(n-1):
    ind = i*(-1)-1
    ind2 = ind-1
    if ls[ind2]<ls[ind]:
        continue
    else:
        x = ls[ind2]
        ind3 = bisect.bisect_right(ls[ind:],x)
        ind4 = ind2+ind3
        ls[ind2], ls[ind4]=ls[ind4],ls[ind2]
        y = ls[ind:]
        y.reverse()
        z = ls[:ind]
        print(*(z+y))
        exit()