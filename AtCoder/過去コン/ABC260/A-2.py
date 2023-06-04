s = input()
if s[0]==s[1] and s[1]==s[2]:
    print(-1)
    exit()

if s[0]==s[1]:
    print(s[2])
    exit()

if s[2]==s[1]:
    print(s[0])
    exit()

if s[0]==s[2]:
    print(s[1])
    exit()

print(s[0])