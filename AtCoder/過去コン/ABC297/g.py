n,l,r = map(int, input().split())
ls = list(map(int,input().split()))

def solve(N1, N2, N3, N4):
    global dp
    Ns = [N1, N2, N3, N4]
    Ntotal = sum(Ns)
    Ns.sort(reverse = True)
    dp = [[[[[-2] * (Ntotal + 1) for n3 in range(Ns[3]+1)] for n2 in range(Ns[2]+1)] for n1 in range(Ns[1]+1)] for n0 in range(Ns[0]+1)]
    for n_player in range(Ntotal + 1):
        if n_player > Ntotal - n_player:
            dp[0][0][0][0][n_player] = 1
        elif n_player == Ntotal - n_player:
            dp[0][0][0][0][n_player] = 0
        else:
            dp[0][0][0][0][n_player] = -1
    return win(0, 0, Ns)

dp = []
def win(n_player, n_opponent, ns):
    '''手番のもちカード数がn_player, 相手のもちカード数がn_opponent
    山のカードの枚数が n0, n1, n2, n3 であるときに、
    自分が勝つならば 1
    相手が勝つならば　-1
    引き分けならば 0
    を返す。
    '''
    global dp
    ns.sort(reverse=True)
    n0, n1, n2, n3 = ns
    if dp[n0][n1][n2][n3][n_player] != -2:
        return dp[n0][n1][n2][n3][n_player]
    record = -1
    for idx in range(4):
        for dn in range(1, 4):
            ns_copy = ns[:]
            ns_copy[idx] -= dn
            if ns_copy[idx] > 0:
                result = win(n_opponent, n_player + dn, ns_copy)
            elif ns_copy[idx] == 0:
                result = win(n_opponent//2, n_player + dn + (n_opponent + 1)//2, ns_copy)
            else:
                break
            if result == -1:
                dp[n0][n1][n2][n3][n_player] = 1
                return 1
            if result == 0 and record == -1:
                record = 0
    dp[n0][n1][n2][n3][n_player] = record
    return record
            
winner = solve(*ls)
if winner == 1:
    print('First')
elif winner == -1:
    print('Second')