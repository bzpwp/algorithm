n,k,q = map(int, input().split())
lsa = list(map(int, input().split()))
lsl = list(map(int, input().split()))

for i in lsl:
    if lsa[i-1]==n:
        continue
    elif lsa[i-1]+1 not in lsa:
        lsa[i-1]+=1
    

print(*lsa)