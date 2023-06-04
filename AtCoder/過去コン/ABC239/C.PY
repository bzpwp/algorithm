x1,y1,x2,y2 = map(int, input().split())
import math
import sys
ls1=[[x1+2,y1+1],[x1+1,y1+2],[x1-1,y1+2],[x1-2,y1+1],[x1-2,y1-1],[x1-1,y1-2],[x1+1,y1-2],[x1+2,y1-1]]
ls2=[[x2+2,y2+1],[x2+1,y2+2],[x2-1,y2+2],[x2-2,y2+1],[x2-2,y2-1],[x2-1,y2-2],[x2+1,y2-2],[x2+2,y2-1]]
for s in ls1:
    if s in ls2:
        print("Yes")
        sys.exit()
print("No")