#!/usr/bin/env python3
from collections import defaultdict
from copy import copy

opcodes = {
    # Addition
    'addr': lambda r, a, b: r[a] + r[b],
    'addi': lambda r, a, b: r[a] + b,

    # Multiplication
    'mulr': lambda r, a, b: r[a] * r[b],
    'muli': lambda r, a, b: r[a] * b,

    # Bitwise
    'banr': lambda r, a, b: r[a] & r[b],
    'bani': lambda r, a, b: r[a] & b,
    'borr': lambda r, a, b: r[a] | r[b],
    'bori': lambda r, a, b: r[a] | b,

    # Assignment
    'setr': lambda r, a, _: r[a],
    'seti': lambda r, a, _: a,

    # Equality
    'gtir': lambda r, a, b: int(a > r[b]),
    'gtri': lambda r, a, b: int(r[a] > b),
    'gtrr': lambda r, a, b: int(r[a] > r[b]),
    'eqir': lambda r, a, b: int(a == r[b]),
    'eqri': lambda r, a, b: int(r[a] == b),
    'eqrr': lambda r, a, b: int(r[a] == r[b]),
}

possible_mappings = defaultdict(set)

# 1

inp1 = open('day16.input1').read().strip().split('\n')

total = 0
for i in range(0, len(inp1), 4):
    before = [int(i) for i in inp1[i][8:].strip('[]').split(', ')]
    inst = tuple(int(i) for i in inp1[i+1].split(' '))
    after = [int(i) for i in inp1[i+2][8:].strip('[]').split(', ')]

    matched = 0
    for code, op in opcodes.items():
        regs = copy(before)
        regs[inst[3]] = op(regs, inst[1], inst[2])

        if regs == after:
            possible_mappings[inst[0]].add(code)
            matched += 1
        else:
            if code in possible_mappings[inst[0]]:
                possible_mappings[inst[0]].remove(code)

    if matched >= 3:
        total += 1

print(total)

# 2

mapping = {}

while possible_mappings:
    for intcode, possible_set in list(possible_mappings.items()):
        if len(possible_set) != 1:
            continue

        mapping[intcode] = possible_set.pop()
        del possible_mappings[intcode]

        for s in possible_mappings.values():
            if mapping[intcode] in s:
                s.remove(mapping[intcode])

inp2 = (
    tuple(int(i) for i in l.split(' '))
    for l in open('day16.input2').read().strip().split('\n')
)

regs = [0, 0, 0, 0]
for inst in inp2:
    regs[inst[3]] = opcodes[mapping[inst[0]]](regs, inst[1], inst[2])

print(regs[0])
