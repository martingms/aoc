#!/usr/bin/env python3

# Input data
inp = 260321
inp_seq = [2, 6, 0, 3, 2, 1]

elf1, elf2 = (0, 1)
recipes = [3, 7]

def match(init, subl, l):
    for i in range(init, len(l) - len(subl) + 1):
        if l[i:i+len(subl)] == subl:
            return i

    return None

while True:
    new = [int(d) for d in str(recipes[elf1] + recipes[elf2])]
    recipes.extend(new)
    elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)

    # 1
    if len(recipes) == inp + 10:
        print(''.join(str(r) for r in recipes[inp:inp+10]))

    # 2
    m = match(len(recipes) - len(new) - len(inp_seq), inp_seq, recipes)
    if m is not None:
        print(m)
        break
