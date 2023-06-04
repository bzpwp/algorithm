from collections import Counter
from itertools import accumulate


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(accumulate(A))
    C = Counter()
    C[0] += 1  # 連続部分列の0番目からi番目を数えるために、0を1個入れる必要があります
    ans = 0
    print(B)
    for x in B:
        y = x - K  # x - y = K より、y = x - K である連続部分列が今まで何回出てきたかが知りたいものです
        ans += C[y]
        C[x] += 1
        print(C)
        print(ans)

    print(ans)


if __name__ == '__main__':
    main()