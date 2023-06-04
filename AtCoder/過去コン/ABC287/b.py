n, m = map(int,input().split())
ls = [input() for _ in range(n)]
lt = set([int(input()) for _ in range(m)])
a = 0
for i in ls:
    if int(i[3:6]) in lt:
        a += 1
print(a)