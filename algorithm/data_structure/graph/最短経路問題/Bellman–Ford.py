## 全部入り
## 最短距離を求め負閉路があれば検出する

INF = float('inf')

V, E = map(int,input().split())    # Vは頂点数、Eは辺数
es = []    # 辺
for _ in range(E):
    # 頂点fromから頂点toへのコストcostの辺
    f, t, c = map(int,input().split())
    es.append([f, t, c])

def bellmanford(s):
    d = [INF] * V
    d[s] = 0
    
    for i in range(V):
        for j in range(E):
            e = es[j]
            if d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                
                # n回目にも更新があるなら負の経路が存在する
                if i == V-1:
                    d[e[1]] = -INF
                    while True:
                        update = False
                        for i in range(len(es)):
                            e = es[i]
                            if d[e[1]] != -INF and d[e[0]] == -INF:
                                d[e[1]] = -INF
                                update = True
                        if not update:
                            break
    return d

D = bellmanford(0)    # 頂点0を始点とする

print(D)