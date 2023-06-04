n = int(input())
ls = list(map(int, input().split()))

x = n
y = 0
while x > 1:
    x = ls[x-2]
    y += 1
print(y)