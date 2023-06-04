r,c = map(int, input().split())

ls = [] 
for i in range(2): 
	ls.append(list(input().split()))

print(ls[r-1][c-1])