n = int(input())
lsa = list(map(int,input().split()))
q = int(input())
lsq = list(map(int,input().split()))

for m in lsq:
    for i in range(2**n):
        x = 0
        for j in range(n):
            if i>>j & 1:
                x += lsa[j]
        if x == m:
            print("yes")
            break
    else:
        print("no")