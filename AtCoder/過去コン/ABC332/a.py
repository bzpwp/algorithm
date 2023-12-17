n,s,k = map(int,input().split())


x = 0
for _ in range(n):
    a,b = map(int,input().split())
    x += a*b
if x < s:
    x += k

print(x)