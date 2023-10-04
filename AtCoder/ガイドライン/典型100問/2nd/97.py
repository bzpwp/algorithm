n,m = map(int,input().split())
ls = list(map(int,input().split()))

# 拡張ユークリッドの互除法
def extgcd(a, b):
    d = a
    if b != 0:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
    else:
        x = 1
        y = 0
    return d, x, y


import math

def ans(a,b,c,d): #c,dは初項
    # c + a*x = d + b*yが成り立つ一般項     # 7 + 14*x = 11 + 22*y
    # a*x - b*y = d - c    # 14*x - 22*y = 4
    e, x1, y1 = extgcd(a, b)
    print(e, x1, y1)
    # a*x1 + b*y1 = e               # 14*(-3) + 22*2 = 2
    # (a/e)*x1 + (b/e)*y1 = 1       # 7*(-3) + 11*2 = 1
    # (a/e)*x - (b/e)*y = (d - c)/e     # 7*x - 11*y = 2
    if (d - c)%e != 0 or ((d - c) != 0 and ((d - c)//e != -1 and (d - c)//e != 1)):
        return False, 0, 0 #解無し
    elif (d - c)//e == 1: #(a/e)*x - (b/e)*y = 1
        #(a/e)(x-x1)=(b/e)(y+y1)    # 3(x-0) = 5(y+(-1))
        #(y+y1) = (a/e)*X   # ((y+(-1)) = 3*X 
        # y = (a/e)*X - y1  # y = 3*X - (-1)
        # d + b*yに代入     # 5 + 10*yに代入
        # d + b*((a/e)*X - y1) #一般項     # 5 + 10*(3*X - (-1))
        # = (a*b)/e * X + d - b*y1
        # max(c, d)以上の最小の項 = 一般項の初項
        # (a*b)/e * X + d - b*y1 >= max(c, d)となる最小のX
        # X >= (max(c, d) - d + b*y1)/((a*b)/e)
        X = math.ceil((max(c, d) - d + b*y1)/((a*b)/e))
        return True, int(d + b*((a/e)*X - y1)), int((a*b)/e) #初項、増分

    elif (d - c)//e == -1: #(a/e)*x - (b/e)*y = 1
            #(a/e)(x+x1)=(b/e)(y-y1)    # 1(x+0) = 1(y-1)
            #(y-y1) = (a/e)*X   # y-1 = X 
            # y = (a/e)*X + y1  # y = X - (-1)
            # d + b*yに代入     # 3 + 6*yに代入
            # d + b*((a/e)*X + y1) #一般項     # 3 + 6*(X - (-1))
            # = (a*b)/e * X + d + b*y1
            # max(c, d)以上の最小の項 = 一般項の初項
            # (a*b)/e * X + d + b*y1 >= max(c, d)となる最小のX
            # X >= (max(c, d) - d - b*y1)/((a*b)/e)
            X = math.ceil((max(c, d) - d - b*y1)/((a*b)/e))
            return True, int(d + b*((a/e)*X + y1)), int((a*b)/e) #初項、増分
    elif (d - c) == 0:
            # (a/e)*x = (b/e)*y     # 3*x = 2*y
            # y = (a/e)*X           # y = 3*X
            # d + b*yに代入         # 3 + 4*yに代入
            # d + b*((a/e)*X) #一般項   # 3 + 4*(3*X)
            # max(c, d)以上の最小の項 = 一般項の初項
            # d + b*((a/e)*X) >= max(c, d)となる最小のX
            # X >= (max(c, d) - d)/((a*b)/e)
            X = math.ceil(max(c, d) - d)/((a*b)/e)
            return True, int(d + b*((a/e)*X)), int((a*b)/e) #初項、増分

a,c = ls[0], ls[0]//2
for i in range(n-1):
    b,d = ls[i+1], ls[i+1]//2
    boo, first, add = ans(a,b,c,d)
    if boo:
        a,c = add,first
    else:
        print(0)
        exit()

if m < first:
    print(0)
else:
    print((m-first)//add + 1)