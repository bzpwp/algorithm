n,x = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()
t = 0
s = 0
if sum(ls)==x:
    print(n)
else:
    for i in range(n):
        if t > x:
            break
        t += ls[i]
        s += 1
    print(s-1)