#!/usr/bin/env python3

from collections import defaultdict

def parse(lines):
    out = []

    for line in lines:
        line = line.split(' ')
        line[0] = 'regs["{}"]'.format(line[0])
        if line[1] == 'inc':
            line[1] = '+='
        else:
            line[1] = '-='
        line[4] = 'regs["{}"]'.format(line[4])
        line.append('else 0')
        out.append(' '.join(line))

    return out

# Input data
inp = open('day8.input').read().strip().split('\n')

# Part One
test = '''
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
'''.strip().split('\n')

regs = defaultdict(int)
for line in parse(test):
    exec(line, globals(), locals())

assert max(regs.values()) == 1

regs = defaultdict(int)
for line in parse(inp):
    exec(line, globals(), locals())

print(max(regs.values()))


# Part Two
mx = []
regs = defaultdict(int)
for line in parse(inp):
    exec(line, globals(), locals())
    mx.append(max(regs.values()))

print(max(mx))
