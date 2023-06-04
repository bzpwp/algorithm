n = int(input())

lsa = []
lsb = []
ans = 0
for i in range(n):
    a,b = map(int,input().split())
    ans += abs(a-b)
    lsa.append(a)
    lsb.append(b)

lsa.sort()
lsb.sort()

c = n//2
xa = lsa[c]
xb = lsb[c]

for i in range(n):
    ans += abs(xa-lsa[i])
    ans += abs(xb-lsb[i])

print(ans)