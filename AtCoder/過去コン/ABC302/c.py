n,m = map(int,input().split())
ls = [input() for _ in range(n)]

def is_one_char_different(word1, word2):
    if len(word1) != len(word2):
        return False
    
    diff_count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_count += 1
            if diff_count > 1:
                return False
    
    return diff_count == 1


from itertools import permutations
for i in permutations(list(range(n))):
    ccc = 0
    for j in range(n-1):
        x = ls[i[j]]
        y = ls[i[j+1]]
        if is_one_char_different(x,y):
            ccc += 1
    if ccc == n-1:
        print("Yes")
        # print(i)
        exit()
print("No")