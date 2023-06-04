import sys
input = sys.stdin.readline
n, q = map(int,input().split())
ls = list(map(int, input().split()))
ls.sort()
for a in range(q):
    x = int(input())
    for b in range(n):
        if ls[n-1] < x:
            print(0)
            break
        elif ls[b] >= x:
            print(n-b)
            break