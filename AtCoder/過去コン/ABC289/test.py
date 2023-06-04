    dp2 = [[-1 for _ in range(n)] for __ in range(n)]
    for a in dd[1]:
        dp2[0][a-1] = lc[a-1]
    for a in range(n):
        for b in range(b):
            if dp2[a][b] >= 0:
                for c in dd[b+1]:
                    if lc[c-1] != dp2[a][b]:
                        dp2[a+1][c-1] = lc[c-1]