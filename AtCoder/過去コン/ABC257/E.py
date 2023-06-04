import itertools
n = int(input())
ls = list(map(int, input().split()))

p = list(itertools.permutations(list(range(1,10)), 9))
def func(a,b):
    return 10*a+b
y = 0
for l in p:
    x = 0
    z = n
    for i in l:
        z -= ls[i-1]
        if z < 0:
            break
        else:
            x = func(x,i)
    y = max(y,x)
    print(y)
print(y)