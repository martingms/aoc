#!/usr/bin/env python3

#def build(lines):
#    tree = {}
#    for line in lines:
#        words = line.split(' ')
#        tree[words[0]] = {
#            'weight': int(words[1][1:-1]),
#            'children': {c.strip(',') for c in words[3:]}
#        }
#
#    return tree

def revbuild(lines):
    lines = [l.split(' ') for l in lines]
    tree = {l[0]:{} for l in lines}
    for line in lines:
        parent = line[0]
        for child in (c.strip(',') for c in line[3:]):
            tree[child]['parent'] = parent

    return tree


def root(tree):
    for n, children in tree.items():
        if len(children) == 0:
            return n

# Input data
inp = open('day7.input').read().strip().split('\n')

# Part One
test = '''
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
'''.strip().split('\n')

assert root(revbuild(test)) == 'tknk'

print(root(revbuild(inp)))


# Part Two
