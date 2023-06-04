from collections import defaultdict

dd = defaultdict(set)

dd[1].add(1)
dd[1].add(2)
print(dd)
dd[1].remove(1)
print(dd)
print(dd[1].pop())
print(len(dd[1]))

del dd[1]
print(dd)