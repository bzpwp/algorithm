n = int(input())
ls = list(map(int, input().split()))
x =[0]
for a in ls:
    x =list(map(lambda i: i+a, x))
    x.insert(0,0)
y = []
for a in x:
    y.append(a%360)
y.sort()
z = 0
l = len(y)
for b in range(l-1):
    z = max(z,y[b+1]-y[b])
z = max(z,360-y[l-1])
print(z)