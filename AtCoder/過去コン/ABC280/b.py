n = int(input())
ls = list(map(int,input().split()))



a = [ls[0]]
x = ls[0]
for i in range(1,n):
    a.append(ls[i]-x)
    x += ls[i]-x
print(*a)