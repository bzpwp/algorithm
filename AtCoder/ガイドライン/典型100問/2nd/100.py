def cal(a):
    return a*(a-1)//2

ls = [cal(i) for i in range(2,500)]
import bisect
n = int(input())
ind = bisect.bisect_left(ls, n)
if n!=ls[ind]:
    print("No")
else:
    ind += 2 #グループの数
    print("Yes")
    print(ind)
    B = 2*n//ind
    A = [[]for _ in range(ind)]
    x = 1
    y = ind-1
    for i in range(ind-1):
        A[i] += [j for j in range(x,x+y)]
        z = x
        for j in range(i+1,i+1+y):
            A[j].append(z)
            z += 1
        x += y
        y -= 1
    for l in A:
        print(B,*l)