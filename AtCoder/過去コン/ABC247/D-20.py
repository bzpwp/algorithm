from collections import deque


q = int(input())
dq = deque()

for i in range(q):
    t, *args = map(int, input().split())
    if t == 1:
        x, c = args
        dq.append((x, c))
        print(dq)
    else:
        c, = args
        ans = 0
        cnt = 0
        while cnt < c:
            a, b = dq.popleft()
            use = min(b, c - cnt)
            cnt += use
            ans += a * use
            if use < b:
                dq.appendleft((a, b - use))
        print(ans)