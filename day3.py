#!/usr/bin/env python3

from math import ceil, sqrt

def squares(n):
    root = ceil(sqrt(n))
    c_len = root if root % 2 != 0 else root + 1
    c_num = (c_len - 1) / 2
    cycle = n - ((c_len - 2) ** 2)
    offset = cycle % (c_len - 1)

    return int(c_num + abs(offset - c_num))

# Input data
inp = int(open('day3.input').read().strip())

# Part One
assert squares(12) == 3
assert squares(23) == 2
assert squares(1024) == 31

print(squares(inp))

# Part Two
# Lookup from https://oeis.org/A141481/b141481.txt
