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

print(find_negative_loop())