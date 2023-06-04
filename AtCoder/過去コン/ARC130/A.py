n = int(input())
s = input()
l = []

for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if (s[:i]+s[i+1:])==(s[:j]+s[j+1:]):
            l.append([i,j])
print(len(l))