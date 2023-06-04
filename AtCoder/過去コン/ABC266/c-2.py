a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = list(map(int,input().split()))

from numpy.linalg import solve

def check(x,y,z,w):
    ex = y[0]-w[0]
    ey = y[1]-w[1]
    fx = z[0]-w[0]
    fy = z[1]-w[1]
    gx = x[0]-w[0]
    gy = x[1]-w[1]

    left = [[ex, fx],
            [ey, fy]]
    
    right = [gx, gy]
    
    s,t = solve(left, right)
    if s > 0 and s < 1 and t > 0 and t < 1 and s + t < 1:
        print("No")
        exit()

check(a,b,d,c)
check(b,c,a,d)
check(c,d,b,a)
check(d,a,c,b)
print("Yes")