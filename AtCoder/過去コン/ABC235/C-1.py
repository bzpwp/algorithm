
n,q = map(int, input().split())
lsa = list(map(int, input().split()))
for i in range(q): 
    x,k = map(int, input().split())
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