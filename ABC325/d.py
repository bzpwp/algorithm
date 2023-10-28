n = int(input())

itv = []

for i in range(n):
    t,d = map(int,input().split())
    itv.append([t+d, t])
print(itv)
itv.sort()

print(itv)

ans = 0
t = 0
for i in range(n):
    if t <= itv[i][1]:
        ans += 1
        t += 1
        print(i)
print(ans)