import sys
input = sys.stdin.readline

n = int(input())
s = input()
l = []
x = 0
y = 0
z = 0
import math
def combinations_count(n):
    return math.factorial(n) // (math.factorial(n - 2) * math.factorial(2))
for i in range(z,len(s)-1):
    y = 0
    if s[i]==s[i+1]:
        x += 1
        while i+1+x<=len(s)-1 and s[i]==s[i+1+x]:
            x +=1
        y += combinations_count(x+1) 
    s = s[:i]+s[i+1+x:]
    z = x
    x = 0
    print(s)
print(y)