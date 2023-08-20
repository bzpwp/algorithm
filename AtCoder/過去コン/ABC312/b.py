n,m = map(int,input().split())
ls = [list(input()) for _ in range(n)]

def check(i,j):
    global n,m,ls
    for a in range(3):
        for b in range(3):
            if ls[i+a][j+b] != "#":
                return False
    for a in range(3):
        if ls[i+a][j+3]!=".":
            return False
    for a in range(4):
        if ls[i+3][j+a]!= ".":
            return False
    for a in range(3):
        for b in range(3):
            if ls[i+6+a][j+6+b] != "#":
                return False
    for a in range(3):
        if ls[i+6+a][j+5]!=".":
            return False
    for a in range(4):
        if ls[i+5][j+5+a]!= ".":
            return False
    return True

for i in range(n-8):
    for j in range(m-8):
        if check(i,j):
            print(i+1,j+1)