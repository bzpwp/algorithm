n = int(input())
lsa = list(map(int,input().split()))


from collections import Counter
count = Counter(lsa)
lss = list(set(lsa))
lss.sort()

for i in range(n):
    try:
        x = lss.pop()
        print(count[x])
    except:
        print(0)