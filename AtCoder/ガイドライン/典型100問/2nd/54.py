n = int(input())
LIS = [int(input())]
import bisect
A = 0
for i in range(n-1):
    x = int(input())
    if LIS[-1] < x:
        LIS.append(x)
    else:
        LIS[bisect.bisect_left(LIS,x)] = x
        A += 1
print(A)