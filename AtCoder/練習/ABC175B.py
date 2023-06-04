n = int(input())
ls = list(map(int,input().split()))
s = 0
for i in range(len(ls)-2):
    for j in range(i+1,len(ls)-1):
        for k in range(j+1,len(ls)):
            if ls[i]!=ls[j] and ls[j]!=ls[k] and ls[k]!=ls[i] and ls[i]+ls[j]>ls[k] and ls[j]+ls[k]>ls[i] and ls[k]+ls[i]>ls[j]:
                s += 1
print(s)
