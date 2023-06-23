p,q = input().split()
ls = [3,1,4,1,5,9]
la = ["A","B","C","D","E","F","G"]
pind = la.index(p)
qind = la.index(q)
if pind > qind:
    pind,qind = qind,pind
print(sum(ls[pind:qind]))