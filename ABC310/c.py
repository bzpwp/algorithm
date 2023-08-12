n = int(input())
A = set()
for i in range(n):
    s = input()
    reversed_s = s[::-1]
    A.add(min(s,reversed_s))
print(len(A))