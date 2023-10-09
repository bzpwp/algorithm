n,m = map(int,input().split())
nl = list(map(int,input().split()))
sl = [input() for i in range(n)]


sorted_problems = [[nl[i],i] for i in range(m)]
sorted_problems.sort(reverse=True)

A = 0
scores = []
for i in range(n):
    a = i+1
    for j in range(m):
        if sl[i][j] == "o":
            a += nl[j]
    scores.append(a)
    A = max(A,a)

# print(scores)

for i in range(n):
    score = scores[i]
    if score == A:
        print(0)
    else:
        x = 0
        s = sl[i]
        check = 0
        while score <= A:
            point, no = sorted_problems[check]
            if s[no] == "x":
                score += point
                x += 1
            else:
                check += 1
        print(x)