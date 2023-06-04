from collections import deque
from collections import deque
from sys import stdin
n,q = map(int, stdin.readline().split())
lsa = list(map(int, stdin.readline().split()))
for i in range(q): 
    x,k = map(int, stdin.readline().split())
    lsq = deque(lsa)
    y = 0 #xが何個あったか
    z = 0 #要素を何個取り出したか
    while len(lsq)>0:
        if y == k:
            break
        a = lsq.popleft() #取り出したもの
        z += 1
        if a == x:
            y += 1
    if y < k:
        print(-1)
    else:
        print(z)