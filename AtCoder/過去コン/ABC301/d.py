s = input()
n  =int(input())

x = bin(n)[2:]

if len(s) < len(x):
    print(int(s.replace("?","1"),2))
    exit()
else:
    a = int(s.replace("?","0"),2)
    if a > n:
        print(-1)
        exit()
    else:
        s = list(s)
        for i in range(len(s)):
            if s[i] == "?":
                a += 2**(len(s)-i-1)
                if a > n:
                    a -= 2**(len(s)-i-1)
print(a)