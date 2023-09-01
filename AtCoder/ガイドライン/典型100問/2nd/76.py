n = int(input())
ls = [0] + list(map(int,input().split()))
import itertools

l = list(itertools.accumulate(ls))
print(l)
for i in range(n):
    a = 0
    for j in range(n-i):
        # if i == 2:
            # print("j",j)
        a = max(a, l[j+i+1]-l[j])
    print(a)