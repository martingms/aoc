from functools import reduce
from operator import mul

inp = open('day3.input').read().strip().split('\n')

def trees(forest, slope):
    trees = 0
    width = len(forest[0])
    column = 0
    for row in range(slope[1], len(forest), slope[1]):
        column += slope[0]
        column %= width
        if inp[row][column] == "#":
            trees += 1

    return trees

print(trees(inp, (3,1)))

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
trees_hit = [trees(inp, slope) for slope in slopes]
print(reduce(mul, trees_hit, 1))
