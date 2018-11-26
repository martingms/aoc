#!/usr/bin/env python3

from itertools import combinations

# Input data
inp = open('day2.input').read().strip().split('\n')
inp = [list(map(int, l.split('\t'))) for l in inp]

# Part One
def checksum(s):
    return sum(map(lambda l: max(l) - min(l), s))

test1 = [
    [5, 1, 9, 5],
    [7, 5, 3],
    [2, 4, 6, 8]
]
assert checksum(test1) == 18

print(checksum(inp))

# Part Two
def divs(l):
    is_divisible = lambda c: max(c) % min(c) == 0
    return next(filter(is_divisible, combinations(l, 2)))

def div_sum(s):
    return sum(map(lambda c: max(c) // min(c), map(divs, s)))

test2 = [
    [5, 9, 2, 8],
    [9, 4, 7, 3],
    [3, 8, 6, 5]
]
assert div_sum(test2) == 9

print(div_sum(inp))
