n,w,d = map(int,input().split())

pieces = [w*d, w, d]

for i in range(n):
    p,s = map(int,input().split())
    piece = piece[p-1]
    S, w, d = piece
    