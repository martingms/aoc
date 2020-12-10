from collections import Counter
from functools import lru_cache
from itertools import takewhile

inp = [int(n) for n in open('day10.input').read().strip().split('\n')]
ratings = [0] + sorted(inp) + [max(inp) + 3]

jumps = Counter(j2 - j1 for j1, j2 in zip(ratings, ratings[1:]))
print(jumps[1] * jumps[3])

@lru_cache(maxsize=len(ratings))
def arrangements(i):
    if i == len(ratings) - 1:
        return 1
    return sum(
        arrangements(j) for j in takewhile(
            lambda j: ratings[j] - ratings[i] <= 3, range(i+1, len(ratings))))

print(arrangements(0))
