n = int(input())
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

A = 0
for i in range(1,n+1,2):
    # print(i)
    a = factorization(i)
    x = 1
    for j in a:
        x *= j[1]+1
    if x == 8:
        A += 1
print(A)
# print(factorization(105))
