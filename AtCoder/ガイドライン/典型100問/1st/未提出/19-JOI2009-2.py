d = int(input())
n = int(input())
m = int(input())
shop = [0]
for i in range(n-1):
    shop.append(int(input()))
ans = 0
shop.sort()
import bisect
for i in range(m):
    point = int(input())
    index = bisect.bisect_left(shop, point)
    if index == n:
        ans += min(d-point,point-shop[-1])
    else:
        ans += min(point-shop[index-1],shop[index]-point)
print(ans)