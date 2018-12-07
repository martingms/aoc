#!/usr/bin/env python3
from collections import defaultdict
from copy import deepcopy

# Input data
inp = open('day7.input').read().strip().split('\n')

def parse(inp):
    for line in inp:
        parts = line.split(' ')
        yield (parts[1], parts[7])

def build_prereqs(steps):
    prereqs = defaultdict(set)
    for step in steps:
        prereqs[step[0]]
        prereqs[step[1]].add(step[0])

    return prereqs

def remove_prereq(prereqs, k):
    for p in prereqs.values():
        if k in p:
            p.remove(k)


steps = list(parse(inp))

#1

out = []
prereqs = build_prereqs(steps)
while prereqs:
    n = min(s for s, p in prereqs.items() if not p)
    out.append(n)
    del prereqs[n]
    remove_prereq(prereqs, n)

print(''.join(out))

# 2

elapsed = 0
prereqs = build_prereqs(steps)
doing = {}
while prereqs or doing:
    finished = set()
    for k in sorted(doing.keys()):
        doing[k] -= 1
        if doing[k] == 0:
            remove_prereq(prereqs, k)
            finished.add(k)

    for k in finished:
        del doing[k]

    cap = 5 - len(doing)
    for n in sorted(s for s, p in prereqs.items() if not p)[:cap]:
        doing[n] = 60 + (ord(n) - 64)
        del prereqs[n]

    elapsed += 1

print(elapsed - 1)
