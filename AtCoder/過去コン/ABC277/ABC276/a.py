s = list(input())
s.reverse()
if "a" not in s:
    print(-1)
else:
    print(len(s)-s.index("a"))