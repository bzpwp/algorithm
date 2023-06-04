import heapq

def dijkstra(edges, num_node, Goal):
    """ 経路の表現
            [終点, 辺の値]
            A, B, C, D, ... → 0, 1, 2, ...とする """
    node = [float('inf')] * num_node    #スタート地点以外の値は∞で初期化
    node[0] = 0     #スタートは0で初期化

    node_name = []
    heapq.heappush(node_name, [0, [0]])

    while len(node_name) > 0:
        #ヒープから取り出し
        _, min_point = heapq.heappop(node_name)
        last = min_point[-1]
        if last == Goal:
            return min_point, node  #道順とコストを出力させている

        #経路の要素を各変数に格納することで，視覚的に見やすくする
        for factor in edges[last]:
            goal = factor[0]   #終点
            cost  = factor[1]   #コスト

            #更新条件
            if node[last] + cost < node[goal]:
                node[goal] = node[last] + cost     #更新
                #ヒープに登録
                heapq.heappush(node_name, [node[last] + cost, min_point + [goal]])

    return []

if __name__ == '__main__':
    n = int(input())
    lsa = list(map(int,input().split()))

    Edges = [[]for _ in range(n)]
    for i in range(n):
        s = input()
        for j in range(n):
            if s[j] == "Y":
                Edges[i].append([j,1])

    node_num = n

    Goal = n-1   
    opt_root, opt_cost = dijkstra(Edges, node_num, Goal)    #道順とコストを出力させている

    #出力を見やすく整理するための変換用辞書型リストの作成
    root_converter = {}
    cost_converter = {}
    for i in range(node_num):
        root_converter[i] = chr(ord('A') + i)
        cost_converter[i] = opt_cost[i]

    arrow = " → "
    result = ""
    for i in range(len(opt_root)):
        if i > 0:
            result += arrow
        result += f"{root_converter[opt_root[i]]}({cost_converter[opt_root[i]]})"

    print(f"ノード(そこまでのコスト)\n\n{result}")