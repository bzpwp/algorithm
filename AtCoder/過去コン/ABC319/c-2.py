from itertools import permutations
A=[]
for _ in range(3):
  A+=list(map(int,input().split()))

cand=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
def check(p):
  # print(p)
  for a,b,c in cand:
    for _ in range(3):
      if A[a]==A[b] and p[a]<p[c] and p[b]<p[c]: 
        print(a,b,c, p)
        return False
      a,b,c=b,c,a
  return True

# print(sum(check(p) for p in permutations(range(9)))/362880)

ord = list(permutations(range(9)))
print(sum(check(p) for p in ord)/362880)

#181 ms