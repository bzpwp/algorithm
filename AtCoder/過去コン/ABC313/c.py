n = int(input())
ls = list(map(int,input().split()))
ls.sort()
# print(ls)
import math
x = sum(ls)/n
a = 0
if x == int(x):
    x = int(x)
    for i in ls:
        a += abs(x-i)
    print(a//2)
else:
    y = math.floor(x)
    z = math.ceil(x)
    # print(y,z)
    numz = sum(ls) - n*y
    numy = n - numz
    # print(numy,numz)
    for i in range(numy):
        a += abs(y-ls[i])
    for i in range(numy, n):
        a += abs(z-ls[i])
    print(a//2)