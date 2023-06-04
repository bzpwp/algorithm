n = int(input())
import bisect
ls = []
l,r = map(int,input().split())
ls.append(l)
ls.append(r)
x = 2
for i in range(n-1):
    l,r = map(int,input().split())
    indexll = bisect.bisect_left(ls, l)
    indexrl = bisect.bisect_left(ls, r)
    if indexll == x:
        ls.append(l)
        ls.append(r)
        x += 2
    elif indexll%2 == 0:
        if indexll == indexrl:
            if indexrl == x:
                ls.append(l)
                ls.append(r)
                x += 2
            elif r == ls[indexrl]:
                ls[indexrl]=l
            else:
                ls.insert(indexrl,r)
                ls.insert(indexrl,l)
                x += 2
        elif indexrl%2==0:
            if indexrl == x:
                del ls[indexll:indexrl]
                ls.append(l)
                ls.append(r)
                x -= indexrl-indexll+2
            elif r == ls[indexrl]:
                del ls[indexll:indexrl+1]
                ls.insert(indexrl,l)
                x -= indexrl-indexll
            else:
                del ls[indexll:indexrl]
                ls.insert(indexll,r)
                ls.insert(indexll,l)
                x -= indexrl-indexll+2
        else:
            del ls[indexll:indexrl]
            ls.insert(indexll,l)
            x -= indexrl-indexll+1

    else:
        if indexrl%2==0:
            del ls[indexll:indexrl]
            ls.insert(indexll,r)
            x -= indexrl-indexll+1
        else:
            del ls[indexll:indexrl]
            x -= indexrl-indexll

x = x//2
for j in range(x):
    print(ls[2*j],ls[2*j+1])