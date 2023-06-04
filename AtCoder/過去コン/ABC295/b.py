r,c = map(int,input().split())
ls = [list(input()) for _ in range(r)]
import copy
ori = copy.deepcopy(ls)
s= set(["1","2","3","4","5","6","7","8","9"])
for h in range(r):
    for i in range(c):
        if ls[h][i] in s:
            b = int(ls[h][i])
            # ori[h][i] = "."
            for a in range(b+1):
                for j in range(a+1):
                    x = j
                    y = a-x
                    # if 
                    ori[min(h+y,r-1)][min(i+x,c-1)] = "."
                    # print("---",a,x)
                    # for l in ori:
                    #     print(''.join(l))
                    ori[max(h-y,0)][min(i+x,c-1)] = "."

                    ori[min(h+y,r-1)][max(i-x,0)] = "."
                    ori[max(h-y,0)][max(i-x,0)] = "."
                    # print("---",a,x,y)
                    # for l in ori:
                    #     print(''.join(l))
for l in ori:
    print(''.join(l))