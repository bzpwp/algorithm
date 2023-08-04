#ベルマンフォード
#入力は支点番号、終点番号、辺の重みのMAP,出力は各辺点最小コスト
#負経路無し
INF = float('inf')

V, E = map(int,input().split())    # Vは頂点数、Eは辺数
es = []    # 辺
for _ in range(E):
    # 頂点fromから頂点toへのコストcostの辺
    f, t, c = map(int,input().split())
    es.append([f, t, c])

d = [INF] * V    # 最短距離

# s番目の頂点から各頂点への最短経路を求める
def shortest_path(s):
    d[s] = 0
    while True:
        update = False
        for i in range(E):
            e = es[i]
            if d[e[0]] != INF and d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                update = True
        if not update:
            break

shortest_path(0)    # 頂点0を始点とする

print(d)




#ベルマンフォード
#入力は支点番号、終点番号、辺の重みのMAP,出力は検出結果
#負経路有り、検出
INF = float('inf')

V, E = map(int,input().split())    # Vは頂点数、Eは辺数
es = []    # 辺
for _ in range(E):
    # 頂点fromから頂点toへのコストcostの辺
    f, t, c = map(int,input().split())
    es.append([f, t, c])

# trueなら負の閉路が存在する
def find_negative_loop():
    d = [0] * V
    
    for i in range(V):
        for j in range(E):
            e = es[j]
            if d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                
                # n回目にも更新があるなら負の経路が存在する
                if i == V-1:
                    return True
    return False

find_negative_loop()






#ベルマンフォード
#入力は支点番号、終点番号、辺の重みのMAP,出力は各辺点最小コスト,不経路があればINF
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