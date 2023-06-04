s = input()

ls = list(s)
from collections import Counter

dd = Counter(ls)

print(dd["v"]+dd["w"]*2)