n,k = map(int,input().split())

ls = []

for i in range(n-k+1):
    print("?",*[i for i in range(i+1, i+1+k)])
    ls.append(int(input()))

for i in range(n-k+1,n):
    print("?",*[i+1 if i+1<=5 else i-n+1 for i in range(i, i+k)])
    ls.append(int(input()))

A1 = [0] + [""]*(n-1)
A2 = [1] + [""]*(n-1)

for i in range(n-1):
    if ls[i] == ls[i+1]:
        print(i, "a")
        if i+k <= n-1:
            A1[i+k] = A1[i]
            A2[i+k] = A2[i]
        else:
            A1[i+k-n] = A1[i]
            A2[i+k-n] = A2[i]
    else:
        print(i, "b")
        if i+k <= n-1:
            A1[i+k] = 1 - A1[i]
            A2[i+k] = 1 - A2[i]
        else:
            A1[i+k-n] = 1 - A1[i]
            A2[i+k-n] = 1 - A2[i]
    print(i, A1)

print("!", *ls)

print(A1)
print(A2)