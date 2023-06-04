
db = deque(lsb.sort())
x = 0
for a in range(n):
    if da.popleft() == db[0]:
        db.popleft()
        x += 1
    else: