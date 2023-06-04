n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)  

colors = [0 for i in range(n)]
def is_bipartite():
    stack = [(0,1)] # (頂点、色)のタプルをスタックする。最初は(頂点0, 黒(1))
    while stack:
        #スタックから最後に追加された(頂点, 色)をpop
        v,color = stack.pop()
        #今いる点を着色
        colors[v] = color
        #今の頂点から行けるところをチェック
        for to in graph[v]:
            #同じ色が隣接してしまったらFalse
            if colors[to] == color:
                    return False
            #未着色の頂点があったら反転した色と共にスタックに積む
            if colors[to] == 0:
                    stack.append((to, -color))
    #調べ終わったら矛盾がないのでTrue
    return True

if not is_bipartite():
    print(0)

else:
        

    from collections import deque

    black = set([0])
    white = set()

    def dfs(T,i,check):
        Q = deque([i])
        q = Q.popleft()
        for c in T[q]:
            if check:
                if c in black or c in white:
                    continue
                else:
                    white.add(c)
                    dfs(graph, c, False)
            else:
                if c in black or c in white:
                    continue
                else:
                    black.add(c)
                    dfs(graph, c, True)

    dfs(graph, 0, True)

    numw = len(white)
    numb = len(black)

    print(graph)
    print(white)
    print(black)

    A = 0
    for i in range(n):
        a = 0
        if i in white:
            for j in graph[i]:
                if j in black:
                    a += 1
            A += numb-a
        else:
            for j in graph[i]:
                if j in white:
                    a += 1
            A += numw-a
    print(A//2)