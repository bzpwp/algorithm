n = int(input())

# 仕事をソートするための配列itv
itv = []

for i in range(n):
    t,d = map(int,input().split())
    itv.append([t, t+d])
print(itv)
itv.sort()
print(itv)

ans = 0
t = 1
for i in range(n):
    if t <= itv[i][1]: #でるまえ
        ans += 1
        if t <= itv[i][0]: #はいるまえ
            t = itv[i][0] + 1
        else:
            t += 1
        print(i,t)
print(ans)