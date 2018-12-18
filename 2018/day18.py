#!/usr/bin/env python3
from collections import defaultdict
from copy import deepcopy
import itertools

# Input data
inp = [list(l) for l in open('day18.input').read().strip().split('\n')]
#inp = [list(l) for l in open('day18.test').read().strip().split('\n')]

def adjacents(state, y, x):
    unfiltered = ((i+y,j+x) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0)
    return (
        (i,j) for i,j in unfiltered if 0 <= i < len(state) and 0 <= j < len(state[0])
    )

def count(state, y, x, t):
    return sum(1 for i,j in adjacents(state, y, x) if state[i][j] == t)

def step(state):
    next_state = deepcopy(state)
    for y in range(len(state)):
        for x in range(len(state[y])):
            if state[y][x] == '.' and count(state, y, x, '|') >= 3:
                next_state[y][x] = '|'
            elif state[y][x] == '|' and count(state, y, x, '#') >= 3:
                next_state[y][x] = '#'
            elif (
                state[y][x] == '#' and
                (
                    count(state, y, x, '#') < 1 or
                    count(state, y, x, '|') < 1
                )
            ):
                next_state[y][x] = '.'

    return next_state

def to_string(state):
    return '\n'.join(''.join(l) for l in state)

def resource_value(state):
    trees, yards = 0, 0
    for row in state:
        for cell in row:
            if cell == '|':
                trees += 1
            elif cell == '#':
                yards += 1

    return trees * yards

# 1

state = deepcopy(inp)
for i in range(1, 1000):
    state = step(state)

    if i == 10:
        print(resource_value(state))
        break

# 2

seen = {}
state = deepcopy(inp)
for i in itertools.count():
    s = to_string(state)
    if s in seen:
        period = i - seen[s]
        for _ in range((1000000000 - seen[s]) % period):
            state = step(state)

        print(f'{resource_value(state)}')
        break

    seen[s] = i
    state = step(state)
