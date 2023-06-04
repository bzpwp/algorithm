n = int(input())
ls = list(map(int,input().split()))

q = int(input())
from collections import defaultdict

dd = defaultdict(int)
for i in range(n):
    dd[i+1]=ls[i]
x = 0
for i in range(q):
    a, *b = input().split()
    a = int(a)
    if a == 1:
        dd = defaultdict(int)
        x = int(*b)
    elif a == 2:
        dd[int(b[0])] += int(b[1])
    else:
        print(dd[int(*b)]+x) 