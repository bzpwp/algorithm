t = int(input())
T = []
x = 1
while x <= 10**18:
    T.append(x)
    x *= 2
# print(T)
import itertools
total = list(itertools.accumulate(T))
import bisect

def A(depth, score):
    



for i in range(t):
    n,x,k = map(int,input().split())
    ind = bisect.bisect_left(total,n) #何段か-1 #木
    ind2 = bisect.bisect_left(total,x) #何段か-1 #対象
    num = n - total[ind] #最下段の数
    A = 0
    if ind2 - ind == k:
        A += 2**k
        #右端
        right = x
        for j in range(k):
            x *= 2
            x += 1
        if x * (2**k) <= n and n <= right:
            A -= n - x * (2**k) + 1
    elif ind2 - ind < k:
        A += 2**k
    
    if 
