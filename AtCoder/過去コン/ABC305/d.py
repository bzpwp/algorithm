n = int(input())
ls = list(map(int,input().split()))
import itertools
ls2 = [ls[i*2]-ls[i*2-1] for i in range(1,n//2+1)]
ls2 = [0] + list(itertools.accumulate(ls2))
q = int(input())
import bisect
for i in range(q):
    l,r = map(int,input().split())
    indl = bisect.bisect_left(ls,l)
    indr = bisect.bisect_left(ls,r)
    if indl == 0:
        indl = 1
    if indr == 0:
        print(0)
    elif indl % 2 == 0 and indr % 2 == 0:
        x = ls2[indr//2] - ls2[indl//2-1]
        print(x-(ls[indr]-r) - (l-ls[indl-1]))
    elif indl % 2 == 1 and indr % 2 == 1:
        print(ls2[indr//2]-ls2[indl//2])
    elif indl % 2 == 0 and indr % 2 == 1:
        x = ls2[indr//2] - ls2[indl//2-1]
        print(x - (l-ls[indl-1]))
    elif indl % 2 == 1 and indr % 2 == 0:
        x = ls2[indr//2] - ls2[indl//2]
        print(x - (ls[indr]-r))