'''
隣接リスト
辺の重み無し
'''
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)  # 有向グラフなら消す
print(graph)  # [[2, 3, 5], ..., [1, 3, 4]]

'''
隣接リスト
辺の重み有り
'''
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n):
    u, v, w = map(int, input().split())
    graph[u-1].append([v-1, w])
    graph[v-1].append([u-1, w])  # 有向グラフなら消す
print(graph)  # [[2, 3], [3, 1], [5, 9]], ..., [...]]



#隣接行列
#辺の重み無し
n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1  # 有向グラフなら消す
print(graph)  # [[0, 1, 1, 0, 1], ..., [1, 0, 1, 1, 0]]

#隣接行列
#辺の重み有り
n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u-1][v-1] = w
    graph[v-1][u-1] = w  # 有向グラフなら消す
print(graph)  # [[0, 2, 3, 0, 1], ..., [2, 0, 3, 0, 0]





#隣接リスト to 隣接行列
#重みなし無向
graph_new = [[0]*n for _ in range(n)]  # 隣接行列
for i, g_i in enumerate(graph):
    for j in g_i:
        graph_new[i][j] = 1
print(graph_new)


#隣接行列 to 隣接リスト
#重みなし無向
graph_new = []
for i in range(n):
    tmp_l = []
    for j in range(n):
        if graph[i][j] > 0:
            tmp_l.append(j)
    graph_new.append(tmp_l)
print(graph_new)






#グラフ理論もろもろ
#https://qiita.com/maskot1977/items/e1819b7a1053eb9f7d61#%E3%82%B0%E3%83%A9%E3%83%95%E7%90%86%E8%AB%96%E3%81%AE%E5%9F%BA%E7%A4%8E---basics-of-graph-theory--


#木構造
#https://www.cqpub.co.jp/hanbai/books/18/18781/18781_9syo.pdf