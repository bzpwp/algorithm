n = int(input())
ls = list(map(int, input().split()))
x = []
y = []
for i in range(n-3):
    for j in range(i,n-2):
        for k in range(j,n-1):
            x.append([sum(ls[:i+1]),sum(ls[i+1:j+1]),sum(ls[j+1:k+1]),sum(ls[k+1:])])
for a in range(len(x)):
    y.append(max(x[a])-min(x[a]))
print(min(y))