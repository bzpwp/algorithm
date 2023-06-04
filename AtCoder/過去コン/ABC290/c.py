n,k = map(int,input().split())
lsa = list(map(int,input().split()))

from collections import Counter

c = Counter(lsa)

# print(c)

# A = 0

for i in range(k):
    if i not in c:
        print(i)
        exit()

# print(k,i)
# if k-1 == i:
print(k)
# else:
    # print(i)