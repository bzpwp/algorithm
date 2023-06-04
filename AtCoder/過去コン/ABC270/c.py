



N,X,Y= map(int, input().split())

G = [[] for i in range(N)]
for i in range(N-1):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    G[x].append(y)
    G[y].append(x)





def EulerTour(n, X, i0):
    done = [0] * n
    Q = [~i0, i0] # 根をスタックに追加
    ET = []
    while Q:
        i = Q.pop()
        if i >= 0: # 行きがけの処理
            done[i] = 1
            ET.append(i)
            for a in X[i][::-1]:
                if done[a]: continue
                Q.append(~a) # 帰りがけの処理をスタックに追加
                Q.append(a) # 行きがけの処理をスタックに追加

        else: # 帰りがけの処理
            ET.append(~i)

    return ET

print(EulerTour(N, X, 0))

tour = EulerTour(N, G, X-1)


# print(tour)

xind = 0
ans = []
for i in tour:
    if i == Y-1:
        ans.append(i+1)
        print(*ans)
        exit()
    else:
        if i == X-1:
            ans = [i+1]
        else:
            ans.append(i+1)