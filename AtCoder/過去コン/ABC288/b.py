n,k = map(int,input().split())
ls = [input() for i in range(n)]

l = ls[:k]

l.sort()

for i in l:
    print(i)