n,k = map(int,input().split())

print("?",*[i for i in range(1,k+1)])

p = int(input())

ls = []

for i in range(n-k):
    print("?",*[i for i in range(i+2, i+2+k)])
    p2 = int(input())

    if p==p2:
        ls.append(0)
    else:
        ls.append(1)

    p = p2

for i in range(1, k):
    print("?",*[i for i in range(n+1-k+i, n+1)])
    p2 = int(input())
    if p==p2:
        ls.append(0)
    else:
        ls.append(1)

    p = p2
ls.append(p2)
print("!", *ls)