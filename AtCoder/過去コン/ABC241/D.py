q = int(input())
A = []
import bisect
for a in range(q):
    qu = input()
    if qu[0] == "1":
        c,x = map(int, qu.split())
        A.insert(bisect.bisect(A,x),x)
    if qu[0] == "2":
        c,x,k = map(int, qu.split())
        y = bisect.bisect_right(A,x)
        if y - k < 0:
            print(-1)
        else:
            print(A[y-k])
    if qu[0] == "3":
        c,x,k = map(int, qu.split())
        y = bisect.bisect_left(A,x)
        if y + k > len(A):
            print(-1)
        else:
            print(A[y+k])