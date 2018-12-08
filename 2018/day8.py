#!/usr/bin/env python3
from collections import namedtuple
from itertools import islice

# Input data
inp = (int(i) for i in open('day8.input').read().strip().split(' '))

Node = namedtuple('Node', ['children', 'meta_entries'])

meta_sum = 0

def parse_node(inp):
    global meta_sum

    n_children = next(inp)
    n_meta_entries = next(inp)

    children = [parse_node(inp) for _ in range(n_children)]
    meta_entries = [int(i) for i in islice(inp, n_meta_entries)]

    meta_sum += sum(meta_entries)

    return Node(children, meta_entries)


root = parse_node(inp)

# 1

print(meta_sum)

# 2

def value(node):
    if not node.children:
        return sum(node.meta_entries)

    return sum(
        value(node.children[i-1])
        for i in node.meta_entries
        if 0 <= i-1 < len(node.children)
    )

print(value(root))
