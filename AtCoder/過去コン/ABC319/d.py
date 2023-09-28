n,m = map(int,input().split())
ls = list(map(int,input().split()))
# print(sum(ls)+a-1)
s = max(ls)
# import itertools
# acc = list(itertools.accumulate(ls))

# print(acc

acc = [ls[0]]
for i in range(n-1):
    acc.append(acc[i]+ls[i+1]+1)
# print(acc)
t = acc[-1]
import bisect
while t - s > 1:
    print(t,s)
    x = (s+t)//2
    y = (s+t)//2

    for i in range(m):
        ind = bisect.bisect_left(acc,y)
        y = acc[ind - 1] + x
        print(y)
        if i != m-1 and y >= acc[-1]:
            t = x
            break
        elif i == m-1:
            if y < acc[-1]:
                s = x
                break
            else:
                t = x
print(s,t)

#[9, 15, 18, 26, 28, 37, 46, 49, 51, 57, 60, 64, 71]