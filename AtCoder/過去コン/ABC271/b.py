n,q  = map(int, input().split())
ls = []
for i in range(n):
    ls.append(list(input().split()))


# print(ls)

for j in range(q):
    # print("-")
    # print(i)
    s,t = map(int, input().split())
    print(ls[s-1][t])