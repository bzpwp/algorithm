n,m = map(int,input().split())
nl = [list(map(int,input().split())) for _ in range(n)]
ml = [list(map(int,input().split())) for _ in range(m)]
import math
A = 10**10
def dist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

if m == 0:
    for i in range(n):
        A = min(A,nl[i][2])
    # for i in range(n-1):
    #     for j in range(i+1,n):
    #         A = min(A,(dist(nl[i][0],nl[i][1],nl[j][0],nl[j][1]))/2)
    print(A)

else:
    for i in range(m):
        for j in range(n):
            A = min(A,dist(ml[i][0],ml[i][1],nl[j][0],nl[j][1])-nl[j][2])

    for i in range(m-1):
        for j in range(i+1,m):
            A = min(A,(dist(ml[i][0],ml[i][1],ml[j][0],ml[j][1]))/2)
    print(A)