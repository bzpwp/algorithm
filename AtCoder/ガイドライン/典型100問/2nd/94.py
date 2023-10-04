N,W,D = map(int,input().split())

pieces = [[W*D, W, D]]

for i in range(N):
    p,s = map(int,input().split())
    piece = pieces[p-1]
    pieces = pieces[:p-1] + pieces[p:]
    S, w, d = piece
    s %= 2*w + 2*d
    if s <= w:
        # pieces[p-1] = [s*d,s,d]
        # pieces.append([(w-s)*d,w-s,d])
        ls = [[s*d,s,d],[(w-s)*d,w-s,d]]
        ls.sort()
        pieces += ls
    elif s <= w+d:
        s -= w
        # pieces[p-1] = [w*s,w,s]
        # pieces.append([w*(d-s),w,d-s])
        ls = [[w*s,w,s],[w*(d-s),w,d-s]]
        ls.sort()
        pieces += ls
    elif s <= 2*w+d:
        s -= w+d
        # pieces[p-1] = [(w-s)*d,w-s,d]
        # pieces.append([s*d,s,d])
        ls = [[(w-s)*d,w-s,d],[s*d,s,d]]
        ls.sort()
        pieces += ls
    elif s <= 2*w+2*d:
        s -= 2*w+d
        # pieces[p-1] = [w*s,w,s]
        # pieces.append([w*(d-s),w,d-s])
        ls = [[w*s,w,s],[w*(d-s),w,d-s]]
        ls.sort()
        pieces += ls
    # print(pieces)
pieces.sort()
print(*[i[0] for i in pieces])