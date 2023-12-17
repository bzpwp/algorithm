n = int(input())

import itertools
all = list(itertools.combinations_with_replacement(list(range(12)), 3))

def add_number(tu):
    x = 0
    for i in tu:
        y = 1
        for j in range(i+1):
            x += y
            y *= 10
    return x
all_numbers = [add_number(t) for t in all]
all_numbers.sort()

print(all_numbers[n-1])