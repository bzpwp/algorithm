n,q = map(int, input().split())
lsx = list(map(int, input().split()))
tree = []
for i in range(n):
    tree.append([])
ls = [1]
for i in range(n-1):
    a, b = map(int, input().split())
    if a in ls:
        tree[a-1].append(b)
        ls.append(b)
    else:
        tree[b-1].append(a)
        ls.append(a)
def search(x):
    num.append(lsx[x-1])
    l = len(tree[x-1])
    if l == 0:
        return
    else:
        for a in range(l):
            search(tree[x-1][a])
for i in range(q):
    v,k=map(int, input().split())
    num = []
    search(v)
    num.sort(reverse=True)
    print(num[k-1])