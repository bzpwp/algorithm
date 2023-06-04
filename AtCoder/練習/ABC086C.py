n = int(input())
ls = []
for i in range(n):
    ls.append(list(map(int,input().split())))
ls.insert(0, [0,0,0])
z = 0
for i in range(n):
    t = ls[i+1][0]-ls[i][0] #時間差
    x = abs(ls[i+1][1]-ls[i][1]) #x差
    y = abs(ls[i+1][2]-ls[i][2]) #y差
    if (t - x - y)%2==0 and (t - x - y)>=0:
        z += 0
    else:
        z += 1
if z == 0:
    print("Yes")
else:
    print("No")
