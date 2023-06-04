n = int(input())
nl = list(map(int,input().split()))
q = int(input())
ql = list(map(int,input().split()))

for m in ql:
    c = False
    for i in range(2**n):
        x = 0
        for j in range(n):
            if (i >> j)&1:
                x += nl[j]
        if x == m:
            c = True
            break
    if c:
        print("yes")
    else:
        print("no")
