n = int(input())
l = list(range(1,2*n+2))
import sys
for i in range(n+1):
    num = int(input())
    if num == 0:
        sys.exit()
    else:
        l.remove(num)
        print(l.pop())
        sys.stdout.flush()