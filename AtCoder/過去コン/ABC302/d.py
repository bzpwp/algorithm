n,m,d = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
X = -1
import bisect
for i in A:
    ind = bisect.bisect_left(B,i+d)
    # if i == 3:
    #     print("ind",ind)
    if ind != m:
        if B[ind] == i+d:
            X = max(X,i*2+d)
        else:
            if ind != 0:
                if B[ind-1] >= i-d:
                    X = max(X,i+B[ind-1])
    else:
        if B[ind-1] >= i-d:
            X = max(X,i+B[ind-1])
print(X)