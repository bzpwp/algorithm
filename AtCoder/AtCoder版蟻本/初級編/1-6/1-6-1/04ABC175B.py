n  = int(input())
ls = list(map(int, input().split()))
import itertools
p = list(itertools.combinations(list(range(n)), 3))
a = 0
for i in p:
    x = ls[i[0]]
    y = ls[i[1]]
    z = ls[i[2]]
    if x != y and y != z and z != x:
        if x + y > z and z + y > x and x + z > y:
            a += 1
print(a)