n = int(input())
ls = list(map(int,input().split()))

x = 0

for i in range(n):
    for j in range(ls[i]):
        m = i+1
        d = j+1
        if len(set(list(str(m)+str(d))))==1:
            x += 1

print(x)