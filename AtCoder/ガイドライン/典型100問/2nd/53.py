n = int(input())

import bisect
LIS = [int(input())]
for i in range(n-1):
    x = int(input())
    if LIS[-1] < x:
        LIS.append(x)
    else:
        LIS[bisect.bisect_left(LIS,x)] = x
print(len(LIS))