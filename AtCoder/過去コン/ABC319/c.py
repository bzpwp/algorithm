import itertools
ord = list(itertools.permutations(list(range(9))))
# print(len(ord))
ls = list(list(map(int,input().split())) for _ in range(3))
# print(ls)

out = []

research = list(itertools.combinations(list(range(3)),2))

for i in range(3):
    l = ls[i]
    for r in research:
        a,b = r
        c = 3-a-b
        if l[a]== l[b]:
            out.append([i*3+a, i*3+b, i*3+c])
            # out.append([i*3+b, i*3+a, i*3+c])
            break

for j in range(3):
    for r in research:
        a,b = r
        c = 3-a-b
        if ls[a][j] == ls[b][j]:
            out.append([a*3+j, b*3+j, c*3+j])
            # out.append([b*3+j, a*3+j, c*3+j])
            break

for r in research:
    a,b = r
    c = 3-a-b
    if ls[a][a] == ls[b][b]:
        out.append([a*3+a, b*3+b, c*3+c])
        # out.append([b*3+b, a*3+a, c*3+c])
        break

for r in research:
    a,b = r
    c = 3-a-b
    if ls[a][2-a] == ls[b][2-b]:
        out.append([2*a+2, 2*b+2, c*2+2])
        # out.append([2*b+2, 2*a+2, c*2+2])
        break

# print(out)
# def gakkari(grid):


# def check(cells):

# print(out)

A = 0
for o in ord:
    # print(o)
    for a,b,c in out:
        # a,b,c = gakkari
        # check = 0
        for _ in range(3):
            if ls[a//3][a%3] == ls[b//3][b%3] and o[a] < o[c] and o[b] < o[c]:
                A +=1
                break
            a,b,c=b,c,a
        else:
            break
            # else:
                
        # else:
        #     break
    # else:
    #     A += 1

print(1- A/362880)

#10516 ms