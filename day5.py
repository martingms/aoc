#!/usr/bin/env python3

from collections import Counter
from operator import methodcaller as method

def exit(words):
    n = 0
    idx = 0
    while True:
        try:
            c = words[idx]
        except IndexError:
            return n
        words[idx] += 1
        idx += c
        n += 1

# Input data
inp = list(map(int, open('day5.input').read().strip().split('\n')))

# Part One
assert exit([0, 3, 0, 1, -3]) == 5

print(exit(inp[:]))

# Part Two

def exit_2(words):
    n = 0
    idx = 0
    while True:
        try:
            c = words[idx]
        except IndexError:
            return n
        if c >= 3:
            words[idx] -= 1
        else:
            words[idx] += 1
        idx += c
        n += 1

assert exit_2([0, 3, 0, 1, -3]) == 10

print(exit_2(inp[:]))
