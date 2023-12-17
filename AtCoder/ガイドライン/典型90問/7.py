n = int(input())
ls = list(map(int,input().split()))
q = int(input())

ls.sort()
import bisect

for _ in range(q):
    b = int(input())
    ind = bisect.bisect_left(ls,b)
    if ind == 0:
        print(ls[0]-b)
    elif ind == n:
        print(b-ls[-1])
    else:
        print(min(ls[ind]-b,b-ls[ind-1]))
        