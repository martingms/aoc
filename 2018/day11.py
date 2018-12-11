#!/usr/bin/env python3
from functools import lru_cache

def power_level(x, y, grid_sn):
    rack_id = x + 10
    l = (rack_id * y + grid_sn) * rack_id
    l = int(str(l)[-3])
    return l - 5

grid_sn = 3999
grid = [
    [power_level(x+1, y+1, grid_sn) for y in range(0, 300)]
    for x in range(0, 300)
]


@lru_cache(maxsize=1024)
def subgrid_sum(x, y, s):
    if s <= 0:
        return 0

    return (
        subgrid_sum(x, y, s-1) +
        grid[x+s-1][y+s-1] +
        sum(grid[x_][y+s-1] for x_ in range(x, x+s-1)) +
        sum(grid[x+s-1][y_] for y_ in range(y, y+s-1))
    )

# 1

m3 = max(
    (
        ((x, y), subgrid_sum(x, y, 3))
        for y in range(0, 297) for x in range(0, 297)
    ),
    key=lambda s: s[1]
)

print(f'{m3[0][0]+1},{m3[0][1]+1}')

# 2

mtot = max(
    (
        max(
            (((x, y, s), subgrid_sum(x, y, s)) for s in range(1, 300-max(x, y))),
            key=lambda s: s[1]
        )
        for y in range(0, 299) for x in range(0, 299)
    ),
    key=lambda m: m[1]
)

print(f'{mtot[0][0]+1},{mtot[0][1]+1},{mtot[0][2]}')
