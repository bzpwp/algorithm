'''
1次元
#https://imoz.jp/algorithms/imos_method.html
'''
# 初期化
table = [0] * T
for i in range(C):
    table[S[i]] += 1 # 入店処理: カウントを 1 増やす
    table[E[i]] -= 1 # 出店処理: カウントを 1 減らす

# シミュレート
#累積和でもok
for i in range(1, T):
    table[i] += table[i - 1]

# 最大値を調べる
M = max(table)


'''
2次元
#https://imoz.jp/algorithms/imos_method.html
'''
# 初期化
tiles = [[0]*W for _ in range(H)]

# 重みの加算 (図 3)
for i in range(N):
    tiles[C[i]][A[i]] += 1
    tiles[C[i]][B[i]] -= 1
    tiles[D[i]][A[i]] -= 1
    tiles[D[i]][B[i]] += 1

# 横方向への累積和 (図 4, 5)
for y in range(H):
    for x in range(1, W):
        tiles[y][x] += tiles[y][x-1]

# 縦方向の累積和 (図 6, 7)
for y in range(1, H):
    for x in range(W):
        tiles[y][x] += tiles[y-1][x]

# 最大値を調べる
tile_max = 0
for y in range(H):
    for x in range(W):
        if tile_max < tiles[y][x]:
            tile_max = tiles[y][x]
