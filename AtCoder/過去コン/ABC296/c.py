n,x = map(int,input().split())
l = list(map(int,input().split()))
import bisect
l.sort()
for i in l:
    y = i+x
    ind = bisect.bisect_left(l,y)
    if ind == n:
        pass
    elif l[ind] == y:
        print("Yes")
        exit()
print("No")