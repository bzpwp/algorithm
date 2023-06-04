n  =int(input())
ls = list(map(int,input().split()))

a = []
import copy

x = ls[0]
a.append(x)
for i in range(1,n):
    y = ls[i]
    for j in range(abs(y-x)-1):
        if y > x:
            a.append(x+1)
            x += 1
        else:
            a.append(x-1)
            x -= 1
    a.append(y)
    x = copy.copy(y)
print(*a)