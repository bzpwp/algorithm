n = int(input())
ls = list(map(int,input().split()))

x = ls[0]
y = 1
rl = []
for i in range(1,n):
    if ls[i]!= x:
        y += 1
        x = 1-x
    else:
        rl.append(y)
        y = 1
rl.append(y)
print(rl)
if len(rl) == 1 or len(rl) == 2:
    print(n)
else:
    A = 0
    for i in range(len(rl)-2):
        A = max(A, rl[i] + rl[i+1] + rl[i+2])
    print(A)

