#!/usr/bin/env python3

from operator import itemgetter

def realloc(banks):
    max_idx, max_bank = max(enumerate(banks), key=itemgetter(1))
    banks[max_idx] = 0

    for i in range(1, max_bank + 1):
        banks[(max_idx + i) % len(banks)] += 1

def count_reps(banks):
    seen = set()
    i = 0

    while True:
        realloc(banks)
        i += 1
        frozen = tuple(banks)
        if frozen in seen:
            return i
        seen.add(frozen)

# Input data
inp = list(map(int, open('day6.input').read().strip().split('\t')))

# Part One
banks = [0, 2, 7, 0]
realloc(banks)
assert banks == [2, 4, 1, 2]
realloc(banks)
assert banks == [3, 1, 2, 3]
realloc(banks)
assert banks == [0, 2, 3, 4]
realloc(banks)
assert banks == [1, 3, 4, 1]
realloc(banks)
assert banks == [2, 4, 1, 2]

print(count_reps(inp))

def count_reps_2(banks):
    seen = {}
    i = 0

    while True:
        realloc(banks)
        i += 1
        frozen = tuple(banks)
        if frozen in seen:
            return i - seen[frozen]
        seen[frozen] = i

# Part Two
print(count_reps_2(inp))
