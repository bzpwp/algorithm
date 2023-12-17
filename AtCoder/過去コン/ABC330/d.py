n = int(input())

grid = [list(input()) for _ in range(n)]


gyou = []
retu = []
where_gyou = []
where_retu = []

for i in range(n):
    x = 0
    ls = []
    for j in range(n):
        if grid[i][j] == "o":
            x += 1
            ls.append(j)
    gyou.append(x)
    where_gyou.append(ls)

for i in range(n):
    x = 0
    ls = []
    for j in range(n):
        if grid[j][i] == "o":
            x += 1
            ls.append(j)
    where_retu.append(ls)
    retu.append(x)

# import itertools

A = 0
for i in range(n):
#     choices = list(itertools.combinations(where_gyou[i],2))
#     for x,y in choices:
#         A += len(where_retu[x]) -1
#         A += len(where_retu[y]) -1
# print(A)
    for j in where_gyou[i]:
        A += (gyou[i] - 1)*(retu[j] - 1)

print(A)