#!/usr/bin/env python3
from collections import defaultdict, namedtuple

# Input data
Claim = namedtuple('Claim', ['cid', 'x1', 'y1', 'x2', 'y2'])

inp = open('day3.input').read().strip().split('\n')

def parse():
    for line in inp:
        cid, _, coords, size = line.split(' ')
        cid = int(cid[1:])
        x, y = [int(v) for v in coords[:-1].split(',')]
        w, h = [int(v) for v in size.split('x')]

        yield Claim(cid, x1=x, y1=y, x2=x+w, y2=y+h)

claims = list(parse())

# 1

fabric_claims = defaultdict(int)
for claim in claims:
    for x in range(claim.x1, claim.x2):
        for y in range(claim.y1, claim.y2):
            fabric_claims[(x, y)] += 1

print(sum(x > 1 for x in fabric_claims.values()))

# 2

def overlaps(c1, c2):
    return c1.x1 < c2.x2 and c1.x2 > c2.x1 and c1.y1 < c2.y2 and c1.y2 > c2.y1

for c1 in claims:
    for c2 in claims:
        if c1.cid == c2.cid:
            continue

        if overlaps(c1, c2):
            break

    else:
        print(f'#{c1.cid}')
        break
