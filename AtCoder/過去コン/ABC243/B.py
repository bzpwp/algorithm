n = int(input())
lsa = list(map(int, input().split()))
lsb = list(map(int, input().split()))
x = 0
for a in lsa:
    if a in lsb:
        x += 1
y = 0
for a in range(n):
    if lsa[a]==lsb[a]:
        y += 1
print(y)
print(x-y)