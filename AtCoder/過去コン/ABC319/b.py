n = int(input())
jl = [i for i in range(1,10) if n%i == 0]
njl = [n//i for i in jl]

# print(jl)
# print(njl)

s = "1"

for i in range(1,n+1):
    for j in njl:
        if i >= j and i%j == 0:
            s += str(n//j)
            break
    else:
        s += "-"
print(s)