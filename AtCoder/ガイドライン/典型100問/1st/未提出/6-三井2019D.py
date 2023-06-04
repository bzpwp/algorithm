n = int(input())
s = input()

ans = set([])
for i in range(1000):
    word = str(0)*(3-len(str(i)))+str(i)
    for j in range(n-2):
        if s[j]==word[0]:
            for k in range(j+1,n-1):
                if s[k]==word[1]:
                    for l in range(k+1,n):
                        if s[l]==word[2]:
                            ans.add(word)

print(len(ans))