n,m = map(int,input().split())
nl = list(map(int,input().split()))
sl = [input() for i in range(n)]


from collections import defaultdict

saiko = 0
scores = defaultdict(int)
for i in range(n):
    s = sl[i]
    score = i+1
    for j in range(m):
        if s[j] == "o":
            score += nl[j]
    scores[i] = score
    saiko = max(saiko, score)

nl = [[nl[i],i] for i in range(m)]
nl.sort()

# print(scores,nl,saiko)
for i in range(n):
    s = sl[i]
    x = 1
    for j in range(m):
        if s[nl[-1-i][1]]!= "o":
            