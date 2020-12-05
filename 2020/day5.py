inp = open('day5.input').read().strip().split('\n')

def find(nrange, partitions):
    for partition in partitions:
        nrange[partition] = nrange[0] + (nrange[1] - nrange[0]) // 2
    return nrange[0]

def id(row, col):
    return row * 8 + col

def decode(code):
    row = find([0, 128], (0 if c == "B" else 1 for c in code[:7]))
    col = find([0, 8], (0 if c == "R" else 1 for c in code[7:]))
    return row, col, id(row, col)

decoded = [decode(code) for code in inp]
print(max(p[2] for p in decoded))

# cheating a bit, found limits by inspection :)
all_seats = {(r,c) for r in range(10, 118) for c in range(8)}
print(id(*(all_seats - {(p[0], p[1]) for p in decoded}).pop()))
