t = int(input())
for i in range(t):
    A = 0
    n = int(input())
    ls = list(map(int,input().split()))
    for j in range(n):
        x = ls[j] % 2
        if x:
            A += 1
        else:
            continue
    print(A)