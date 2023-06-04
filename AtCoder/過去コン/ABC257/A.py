

n,x = map(int, input().split())
wls = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


y = x//n
z = x%n
if z == 0:
    print(wls[y-1])
else:
    print(wls[y])