#!/usr/bin/env python3

# Input data
inp = open('day5.input').read().strip()

def react(l):
    i = 0
    while True:
        if i >= len(l) - 1:
            break
        elif abs(ord(l[i]) - ord(l[i+1])) == 32:
            del l[i:i+2]
            if i > 0:
                i -= 1
        else:
            i += 1

    return l

# 1

print(len(react(list(inp))))

# 2

print(min(len(react([v for v in list(inp) if v.lower() != u])) for u in set(inp.lower())))
