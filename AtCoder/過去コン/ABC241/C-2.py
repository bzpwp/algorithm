n = int(input())
ls = [input() for _ in range(n)]
import sys

for s in ls:
    for a in range(n-5):
        if s[a:a+6].count('.') <= 2:
            print("Yes")
            sys.exit()

for b in range(n):
    x = 0
    for a in range(n-5):
        if ls[a][b] == ".":
            x += 1
        if ls[a+1][b] == ".":
            x += 1
        if ls[a+2][b] == ".":
            x += 1
        if ls[a+3][b] == ".":
            x += 1
        if ls[a+4][b] == ".":
            x += 1
        if ls[a+5][b] == ".":
            x += 1
    if x <= 2:
        print("Yes")
        sys.exit()

for a in range(n-5):
    x = 0
    for b in range(n-5):
        if ls[a][b] == ".":
            x += 1
        if ls[a+1][b+1] == ".":
            x += 1
        if ls[a+2][b+2] == ".":
            x += 1
        if ls[a+3][b+3] == ".":
            x += 1
        if ls[a+4][b+4] == ".":
            x += 1
        if ls[a+5][b+5] == ".":
            x += 1
    if x <= 2:
        print("Yes")
        sys.exit()

for a in range(n-5):
    x = 0
    for b in range(5,n):
        if ls[a][b] == ".":
            x += 1
        if ls[a+1][b-1] == ".":
            x += 1
        if ls[a+2][b-2] == ".":
            x += 1
        if ls[a+3][b-3] == ".":
            x += 1
        if ls[a+4][b-4] == ".":
            x += 1
        if ls[a+5][b-5] == ".":
            x += 1
    if x <= 2:
        print("Yes")
        sys.exit()

print("No")