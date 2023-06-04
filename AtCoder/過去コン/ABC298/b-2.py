n = int(input())

import numpy as np

lsa = np.array([list(map(int,input().split())) for _ in range(n)])
lsb = np.array([list(map(int,input().split())) for _ in range(n)])

if np.array_equal(lsa,lsb):
    print("Yes")
    exit()

print(lsa)
print(lsb)
print("------")


for i in range(3):
    lsa = np.rot90(lsa)
    print("------")
    print(lsa)
    print(lsb)
    if np.array_equal(lsa,lsb):
        print("Yes")
        exit()
print("No")