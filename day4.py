#!/usr/bin/env python3

from collections import Counter
from operator import methodcaller as method

def valid(words):
    return max(Counter(words).values()) == 1

# Input data
inp = open('day4.input').read().strip().split('\n')
inp = [l.split(' ') for l in inp]

# Part One
print(sum(map(valid, inp)))

# Part Two
sorted_inp = [[''.join(sorted(w)) for w in l] for l in inp]
print(sum(map(valid, sorted_inp)))
