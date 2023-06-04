n,a,b = map(int, input().split())
total1 = 0
total2 = 0
for i in range(n+1):
    x = i
    y = i
    while x != 0:
        total1 += x%10
        x = x//10
    if a<=total1<=b:
        total2 += y
    total1 = 0
print(total2)