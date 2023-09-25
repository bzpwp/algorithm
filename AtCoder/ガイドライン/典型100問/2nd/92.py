h = int(input())
nl = [list(map(int,input().split())) for _ in range(h)]

A = 0

def delete():
    global A
    check = False
    for a in range(h):
        if nl[a][0]!= -1 and all(i == nl[a][0] for i in nl[a]):
            A += 5*nl[a][0]
            nl[a] = [0]*5
            check = True
        else:
            for b in range(2):
                # print(i,nl[a])
                # print(check)
                if nl[a][b:b+4][0]!= -1 and all(i == nl[a][b:b+4][0] for i in nl[a][b:b+4]):
                    A += 4*nl[a][b]
                    nl[a][b:b+4] = [0]*4
                    check = True

            for b in range(3):
                if nl[a][b:b+3][0] != -1 and all(i == nl[a][b:b+3][0] for i in nl[a][b:b+3]):
                    A += 3*nl[a][b]
                    nl[a][b:b+3] = [0]*3
                    check = True
    return check

def down():
    for a in range(h):
        for b in range(5):
            if nl[h-1-a][b] == 0:
                # print("---")
                # print(nl[h-1-a],h-1-a,a,b)
                for c in range(a,h-1):
                    # print(nl[h-2-c][b],h-2-c,c)
                    nl[h-1-c][b] = nl[h-2-c][b]
                nl[0][b] = -1
    
def check():
    for a in range(h):
        if 0 in nl[a]:
            return True
    return False
print(nl)
while True:
    if not delete():
        break
    while check():
        down()
    print(nl)
    print(A)
print(A)
