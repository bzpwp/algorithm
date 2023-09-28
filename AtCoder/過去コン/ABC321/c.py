n = int(input())

# import math
# c = [9]
# for i in range(2,11):
#     c.append(math.comb(10, i))

import itertools
# acc = list(itertools.accumulate(c))
# import bisect
# ind = bisect.bisect_left(acc,n) #何桁
# num = n - acc[ind] #何番目

# print(acc)

ls = [i for i in range(1,10)]
num = [i for i in range(10)]
for i in range(2,11): #桁
    l = [sorted(list(i), reverse=True) for i in list(itertools.combinations(num,i))]
    l = sorted([int("".join(str(j) for j in i)) for i in l])
    # print(l)
    # print(len(l))
    ls += l
print(ls[n-1])