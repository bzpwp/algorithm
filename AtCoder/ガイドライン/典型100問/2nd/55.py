n = int(input())
import bisect
LIS = [int(input())]
for i in range(n-1):
    x = int(input())
    ind = bisect.bisect_left(LIS, x)
    if ind == 0:
        LIS.insert(0, x)
    else:
        LIS[ind-1] = x
print(len(LIS))
