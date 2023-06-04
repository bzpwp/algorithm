n,k = map(int,input().split())
x = 0
while True:
    if n//k==0:
        break
    n = n//k
    x += 1
print(x+1)
