s = input()

if s[0]!="0":
    print("No")
    exit()
else:
    x = 0
    ls = [[7],[4],[2,8],[1,5],[3,9],[6],[10]]
    for i in range(5):
        for j in range(i+2,7):
            if len(ls[i])==1:
                if s[ls[i][0]-1]=="0":
                    continue
            else:
                if s[ls[i][0]-1]=="0" and s[ls[i][1]]=="0":
                    continue

            if len(ls[j])==1:
                if s[ls[j][0]-1]=="0":
                    continue
            else:
                if s[ls[j][0]-1]=="0" and s[ls[j][1]]=="0":
                    continue

            for k in range(i+1,j):
                if len(ls[k])==1:
                    if s[ls[k][0]-1]=="0":
                        continue
                    else:
                        print("Yes")
                        exit()
                else:
                    if s[ls[k][0]-1]=="1" and s[ls[k][1]-1]=="1":
                        print("Yes")
                        exit()
                    else:
                        continue

print("No")