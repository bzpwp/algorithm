from sys import stdin
def input():
    return stdin.readline().rstrip("\n")

h, w = map(int, input().split())
s = [input() for i in range(h)]
t = [input() for i in range(h)]
print(s)
print(t)
print(zip(*s))
print(zip(*t))
st = sorted(zip(*s))
tt = sorted(zip(*t))
print(st)
print(tt)

cond = st == tt

print("Yes" if cond else "No")




