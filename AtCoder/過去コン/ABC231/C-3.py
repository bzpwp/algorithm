import sys
input = sys.stdin.readline
n, q = map(int,input().split())
ls = list(map(int, input().split()))
ls.sort()
ls1 = [int(input()) for _ in range(q)]
for i in range(q):
    print(sum(y>=ls1[i] for y in ls))