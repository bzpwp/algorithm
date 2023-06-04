n = int(input())
ls = list(map(int, input().split()))
x = 0
while True:
    if x == n-1:
        break
    elif ls[x]<ls[x+1]:
        x +=1
    else:
        break
print(ls[x])