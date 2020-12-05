from itertools import combinations

inp = [int(x) for x in open('day1.input').read().strip().split('\n')]

for x,y,z in combinations(inp, 3):
    if x + y + z == 2020:
        print(x*y*z)
        break
