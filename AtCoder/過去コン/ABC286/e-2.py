# warshall_floyd法
def warshall_floyd(d,v):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k]+d[k][j]:
                    v[i][j] = v[i][k] + lsa[j]
                elif d[i][j] < d[i][k]+d[k][j]:
                    v[i][j] = v[i][j] + lsa[j]
                elif d[i][j] == d[i][k]+d[k][j]:
                    v[i][j] = max(v[i][j] + lsa[j],v[i][k] + lsa[j])
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])

    return d

# n:頂点数　m:辺の数
n = int(input())
lsa = list(map(int,input().split()))

# 隣接行列の定義、初期化
# ①コスト(存在しないときはinf)
d = [[float("inf") for i in range(n)] for i in range(n)]
v = [[0 for i in range(n)] for i in range(n)]
# for i in range(n):
#     a = lsa[i]
#     for j in range(n):
#         v[j] = a

# ②自分自身へのコストは０
for i in range(n):
    d[i][i] = 0

# コスト入力（何もないときは１，問題によっては入力時に指定される）
cost = 1
for i in range(n):
    s = input()
    for j in range(n):
        if s[j]=="Y":
            d[i][j] = cost

warshall_floyd(d,v)

q = int(input())
for i in range(q):
    u,V = map(int,input().split())
    if d[u-1][V-1] == float("inf"):
        print("Impossible")
    else:
        print(d[u-1][V-1], v[u-1][V-1] + lsa[u-1])