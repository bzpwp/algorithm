n, q = map(int,input().split())
ls = list(map(int, input().split()))
for a in range(q):
    s = 0
    x = int(input())
    for b in range(n):
        if ls[b] >= x:
            s += 1
    print(s)