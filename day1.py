#!/usr/bin/env python3

def captcha(s, j):
    inp = list(map(int, s))
    return sum(inp[i] for i in range(len(inp))
               if inp[i] == inp[(i + j) % len(inp)])

# Input data
inp = open('day1.input').read().strip()

# Part One
p1 = lambda s: captcha(s, 1)

assert p1('1122') == 3
assert p1('1111') == 4
assert p1('1234') == 0
assert p1('91212129') == 9

print(p1(inp))

# Part Two
p2 = lambda s: captcha(s, len(s) // 2)

assert p2('1212') == 6
assert p2('1221') == 0
assert p2('123425') == 4
assert p2('123123') == 12
assert p2('12131415') == 4

print(p2(inp))
