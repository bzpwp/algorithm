n = int(input())
ls = set(map(int, input().split()))
ls1 = list(range(2001))
for a in ls1:
    if a not in ls:
        print(a)
        exit()