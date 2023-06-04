lsa = []
for i in range(3):
    lsa.append(list(map(int,input().split())))
n = int(input())
lsb = [int(input()) for _ in range(n)]
if lsa[0][0] in lsb and lsa[0][1] in lsb and lsa[0][2] in lsb:
    print("Yes")
elif lsa[1][0] in lsb and lsa[1][1] in lsb and lsa[1][2] in lsb:
    print("Yes")
elif lsa[2][0] in lsb and lsa[2][1] in lsb and lsa[2][2] in lsb:
    print("Yes")
elif lsa[0][0] in lsb and lsa[1][0] in lsb and lsa[2][0] in lsb:
    print("Yes")
elif lsa[0][1] in lsb and lsa[1][1] in lsb and lsa[2][1] in lsb:
    print("Yes")
elif lsa[0][2] in lsb and lsa[1][2] in lsb and lsa[2][2] in lsb:
    print("Yes")
elif lsa[0][0] in lsb and lsa[1][1] in lsb and lsa[2][2] in lsb:
    print("Yes")
elif lsa[0][2] in lsb and lsa[1][1] in lsb and lsa[2][0] in lsb:
    print("Yes")
else:
    print("No")