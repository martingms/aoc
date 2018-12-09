#!/usr/bin/env python3
from collections import defaultdict, deque
from itertools import count, cycle

# Input data
inp = open('day9.input').read().strip().split(' ')

players, last_marble = int(inp[0]), int(inp[6])

def play(players, last_marble):
    circle = deque([0])
    scores = defaultdict(int)
    for m, p in enumerate(cycle(range(1, players + 1)), 1):
        if m % 23 == 0:
            circle.rotate(7)
            scores[p] += m + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(m)

        if m == last_marble:
            break

    return scores

# 1

print(max(play(players, last_marble).values()))

# 2

last_marble *= 100
print(max(play(players, last_marble).values()))
