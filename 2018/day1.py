#!/usr/bin/env python3
import itertools

# Input data
inp = [int(x) for x in open('day1.input').read().strip().split('\n')]

# 1

print(sum(inp))

# 2

seen = set()
s = 0
for line in itertools.cycle(inp):
    s += line

    if s in seen:
        print(s)
        break

    seen.add(s)
