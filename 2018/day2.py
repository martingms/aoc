#!/usr/bin/env python3
from collections import Counter
from itertools import combinations

# Input data
inp = list(open('day2.input').read().strip().split('\n'))

# 1

twos, threes = 0, 0
for box_id in inp:
    s = set(Counter(box_id).values())
    twos += 2 in s
    threes += 3 in s

print(twos * threes)

# 2

for id1, id2 in combinations(inp, 2):
    z = list(zip(id1, id2))
    if sum(c1 != c2 for c1, c2 in z) == 1:
        print(''.join([c1 for c1, c2 in z if c1 == c2]))
        break
