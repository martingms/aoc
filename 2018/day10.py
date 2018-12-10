#!/usr/bin/env python3
from itertools import count

inp = open('day10.input').read().strip().split('\n')

class Point:
    def __init__(self, x, y, vx, vy):
        self.x, self.y, self.vx, self.vy = x, y, vx, vy

def parse(inp):
    for line in inp:
        line = line[10:].split(',')
        x = int(line[0])
        y = int(line[1].split('>')[0])
        vx = int(line[1].split('<')[-1])
        vy = int(line[2][:-1])

        yield Point(x, y, vx, vy)

points = list(parse(inp))

def pp(points):
    xpoints = sorted(points, key=lambda p: p.x)
    minx, maxx = xpoints[0].x, xpoints[-1].x

    ypoints = sorted(points, key=lambda p: p.y)
    miny, maxy = ypoints[0].y, ypoints[-1].y

    point_coords = {(p.x, p.y) for p in points}

    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if (x, y) in point_coords:
                print('#', end='')
            else:
                print(' ', end='')

        print()

for sec in count(1):
    ys = set()
    for p in points:
        p.x += p.vx
        p.y += p.vy

        ys.add(p.y)

    # Character height found by trial and error :shrug:
    if len(ys) == 10:
        # 1
        pp(points)

        # 2
        print(sec)
        break
