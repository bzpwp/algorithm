# 3x3のサンプルリスト
grid = list(list(map(int,input().split())) for _ in range(3))


# 縦、横、斜めの組み合わせを検索する関数
def find_matches(grid):
    matches = []

    # 縦の組み合わせを検索
    for col in range(3):
        for row in range(1, 3):
            if grid[row][col] == grid[row - 1][col]:
                matches.append(((row - 1, col), (row, col)))

    # 横の組み合わせを検索
    for row in range(3):
        for col in range(1, 3):
            if grid[row][col] == grid[row][col - 1]:
                matches.append(((row, col - 1), (row, col)))

    # 斜めの組み合わせを検索（左上から右下）
    for i in range(1, 3):
        if grid[i][i] == grid[i - 1][i - 1]:
            matches.append(((i - 1, i - 1), (i, i)))

    # 斜めの組み合わせを検索（左下から右上）
    for i in range(1, 3):
        if grid[2 - i][i] == grid[2 - i + 1][i - 1]:
            matches.append(((2 - i + 1, i - 1), (2 - i, i)))

    return matches

# 結果を表示
matches = find_matches(grid)
for match in matches:
    print(match)
