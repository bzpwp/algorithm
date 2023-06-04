n = int(input())
ls = [None] * n
lt = []
x = 0
y = 0
for i in range(n):
    s,t = input().split()
    t = int(t)
    if t > x:
        if s not in set(ls):
            x = t
            y = i
    ls[i]=s

print(y+1)