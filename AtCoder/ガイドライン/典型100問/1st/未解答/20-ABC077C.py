n = int(input())
lsa = list(map(int,input().split()))
lsb = list(map(int,input().split()))
lsc = list(map(int,input().split()))

lsa.sort()
lsb.sort()
lsc.sort()

import bisect
ans = 0
inb = 0
inc = 0
for a in lsa:
    inb += bisect.bisect_right(lsb[inb:],a)
    if inb == n:
        print(ans)
        exit()
    else:
        for b in lsb[inb:]:
            inc += bisect.bisect_right(lsc[inc:],b)
            if lsc == n:
                print(ans)
                exit()
            else:
                ans += n-inc

print(ans)
