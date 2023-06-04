h,w,rs,cs = map(int, input().split())
grid = [["."]*w for _ in range(h)]
n = int(input())
for i in range(n):
    r,c =  map(int, input().split())
    grid[r-1][c-1]="#"
print(grid)
q = int(input())
for i in range(q):
    d,l = input().split()
    l = int(l)
    if d == "L":
        for i in range(l):
            if cs == 1 or grid[rs-1][cs-2]=="#":
                break
            else:
                cs -= 1
    elif d == "R":
        for i in range(l):
            if cs == w or grid[rs-1][cs]=="#":
                break
            else:
                cs += 1
    elif d == "U":
        for i in range(l):
            if rs == 1 or grid[rs-2][cs-1]=="#":
                break
            else:
                rs -= 1
    elif d == "D":
        for i in range(l):
            if rs == h or grid[rs][cs-1]=="#":
                break
            else:
                rs += 1

    # print(rs,cs)