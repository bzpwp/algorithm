k = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

a = factorization(k)

A = 0
for l in a:
    x,y = l
    z = 1
    v = 1
    for i in range(1,y):
        z += 1
        a1 = factorization(k+1)
        for j in a1:
            if j[0]==x:
                z += j[1]
                break
        if z >= y:
            v = i+1
            break
    
    A = max(A,x*v)
print(A)
