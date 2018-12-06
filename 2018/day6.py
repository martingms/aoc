#!/usr/bin/env python3
import sys
from collections import Counter, defaultdict, namedtuple

# Input data
inp = open('day6.input').read().strip().split('\n')

Coord = namedtuple('Coord', ['cid', 'x', 'y'])

def coords_gen(inp):
    for i, line in enumerate(inp):
        x, y = line.split(', ')
        yield Coord(cid=i, x=int(x), y=int(y))

coords = list(coords_gen(inp))

def dist(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

x_sorted = sorted(coords, key=lambda c: c.x)
x_min, x_max = x_sorted[0].x, x_sorted[-1].x
y_sorted = sorted(coords, key=lambda c: c.y)
y_min, y_max = y_sorted[0].y, y_sorted[-1].y

# 1

closest = defaultdict(int)
for x in range(x_min, x_max+1):
    for y in range(y_min, y_max+1):
        min_coord, min_dist = None, sys.maxsize
        for c in coords:
            d = dist(Coord(None, x, y), c)
            if d == min_dist:
                min_coord = None
            if d < min_dist:
                min_coord, min_dist = c, d

        if (
            min_coord is not None and
            min_coord.x not in { x_min, x_max } and
            min_coord.y not in { y_min, y_max }
        ):
            closest[(x, y)] = min_coord.cid


print(max(Counter(closest.values()).items(), key=lambda c: c[1])[1])

# 2

sz = 0
for x in range(x_min, x_max+1):
    for y in range(y_min, y_max+1):
        if sum(dist(Coord(None, x, y), c) for c in coords) < 10000:
            sz += 1

print(sz)
