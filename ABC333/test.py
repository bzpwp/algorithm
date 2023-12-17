import sys
sys.setrecursionlimit(10 ** 9)
def dfs(G, v, p, d, depth, subtree_size):
    depth[v] = d
    for nv in G[v]:
        if nv == p:
            continue
        dfs(G, nv, v, d + 1, depth, subtree_size)

    # 帰りがけ時に、部分木サイズを求める
    subtree_size[v] = 1  # 自分自身
    for c in G[v]:
        if c == p:
            continue
        subtree_size[v] += subtree_size[c]  # 子のサイズを加える

def main():
    # 頂点数 (木なので辺数は N-1 で確定)
    N = int(input())

    # グラフ入力受け取り
    G = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    # 探索
    root = 0  # 仮に頂点 0 を根とする
    depth = [0] * N
    subtree_size = [0] * N
    dfs(G, root, -1, 0, depth, subtree_size)

    # 結果の出力
    sizes = [subtree_size[v] for v in G[0]]
    sizes.sort()
    x = 1
    for i in range(len(sizes)-1):
        x += sizes[i]
    print(x)
    

if __name__ == "__main__":
    main()
