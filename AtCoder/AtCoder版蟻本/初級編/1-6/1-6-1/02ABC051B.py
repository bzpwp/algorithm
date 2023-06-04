k,s = map(int,input().split())
x = 0
for a in range(0,k+1):
    for b in range(0,k+1):
        if s-a-b>=0 and k>=s-a-b:
            x +=1
print(x)