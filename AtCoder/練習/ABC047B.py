w,h,n=map(int,input().split())
ls = [list(map(int,input().split())) for i in range(n)] 
xmaxls = [0]
for a in range(n):
    if ls[a][2]==1:
        xmaxls.append(ls[a][0])
xmax= max(xmaxls)
xminls = [w]
for a in range(n):
    if ls[a][2]==2:
        xminls.append(ls[a][0])
xmin= min(xminls)
ymaxls = [0]
for a in range(n):
    if ls[a][2]==3:
        ymaxls.append(ls[a][1])
ymax= max(ymaxls)
yminls = [h]
for a in range(n):
    if ls[a][2]==4:
        yminls.append(ls[a][1])
ymin= min(yminls)
if xmax >=xmin or ymax >=ymin:
    print(0)
else:
    print((xmin-xmax)*(ymin-ymax))
