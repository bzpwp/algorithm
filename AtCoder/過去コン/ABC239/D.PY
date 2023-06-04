import sys
a,b,c,d = map(int, input().split())
pls=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
plss = set(pls)
for x in range(a,b+1):
    z = 0
    for y in range(c,d+1):
        if x + y not in pls:
            z +=1
        if z == d-c+1:
            print("Takahashi")
            sys.exit()
print("Aoki")