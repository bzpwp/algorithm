import sys
input = sys.stdin.readline
n, q = map(int,input().split())
ls = list(map(int, input().split()))
ls.sort()
for a in range(q):
    x = int(input())
    print(sum(y>=x for y in ls))
    