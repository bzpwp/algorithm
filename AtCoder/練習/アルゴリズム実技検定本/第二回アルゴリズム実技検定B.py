s = input()
import collections
c = collections.Counter(s)
print(max(c,key=c.get))