x,k = map(int, input().split())
for i in range(k):
    x += 1
    x = round(x,-i-1)
print(x)