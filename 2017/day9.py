#!/usr/bin/env python3

from collections import defaultdict

def parse(s, score=0):
    if s[0] = '{':
        return parse(takewhile(lambda c: c != '}', s[1:]), score + 1)

# Input data
inp = open('day9.input').read().strip().split('\n')

# Part One
