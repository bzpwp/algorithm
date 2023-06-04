from collections import deque
from sys import stdin
n,q = map(int, stdin.readline().split())
lsa = list(map(int, stdin.readline().split()))
for i in range(q): 
    x,k = map(int, stdin.readline().split())
    y = 0 #xが何個あったか
    a = 0 #どこまで探索したか
    while a<=n-1:
        if y == k:
            break
        if lsa[a] == x:
            y += 1
        a += 1
    if y < k:
        print(-1)
    else:
        print(a)