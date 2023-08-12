w,h = map(int,input().split())
grid = [[0 for _ in range(w+2)]]
for i in range(h):
    grid.append([0] + list(map(int,input().split())) + [0])
grid.append([0 for _ in range(w+2)])

from collections import deque

dd = deque([[0,0]])
mv1 = [[-1,-1],[-1,0],[-1,1],[0,1],[0,-1],[1,0]] #yが偶数
mv2 = [[1,-1],[-1,0],[1,1],[0,1],[0,-1],[1,0]] #yが奇数
A = 0
grid[0][0] = "X"
counter = [[0 for _ in range(w+2)] for __ in range(h+2)]
while dd:
    y,x = dd.popleft()
    # grid[y][x] = "X"
    if y%2 == 0:
        for mx,my in mv1:
            if w+1>=x+mx>=0 and h+1>=y+my>=0 and grid[y+my][x+mx]!= "X":
                if grid[y+my][x+mx]== 1:
                    # counter[y+my][x+mx] += 1
                    # if y+my == 1 and x+mx == 2:
                    #     print("--",y,x)
                    #     print(grid[y][x])
                    #     print(grid[y+my][x+mx])
                    A += 1
                else:
                    dd.append([y+my,x+mx])
                    grid[y+my][x+mx]= "X"
    else:
        for mx,my in mv2:
            if w+1>=x+mx>=0 and h+1>=y+my>=0 and grid[y+my][x+mx]!= "X":
                if grid[y+my][x+mx] == 1:
                    # counter[y+my][x+mx] += 1
                    # if y+my == 1 and x+mx == 2:
                    #     print("--",y,x)
                    #     print(grid[y][x])
                    #     print(grid[y+my][x+mx])
                    A += 1
                else:
                    dd.append([y+my,x+mx])
                    grid[y+my][x+mx]= "X"
# for i in grid:
#     print(i)
print(A)
# for i in counter:
#     print(i)