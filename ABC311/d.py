n,m = map(int,input().split())
grid = [input() for _ in range(n)]

x = 0
def func(s,dist,point,grid):
    if point[0] in s[point[0]]:
        x = max(x,dist)
    else:

        for i in ["U","D","R","L"]:
            new_point, new_dist = move(i, dist, point)
            
def move(m,d,p):
    if m == "U":

    return new_point, new_dist

from collections import defaultdict

dd = defaultdict(set)
