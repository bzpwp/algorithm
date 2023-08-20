n = int(input())
ls = list(map(int,input().split()))

x = (sum(ls)+1)//2

y = 0
for i in range(n):
    if y<=x<=y + ls[i]:
        print(i+1, x-y)
        exit()
    else:y += ls[i]