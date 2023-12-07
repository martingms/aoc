inp = open("day5.test").read().strip().split("\n\n")
#inp = open("day5.input").read().strip().split("\n\n")

# 1

seeds = [int(s) for s in inp[0].split()[1:]]
def parse_map(s): return [[int(n) for n in l.split()] for l in s.split("\n")[1:]]
maps = [parse_map(s) for s in inp[1:]]

def next(value, map):
    for dstart, sstart, length in map:
        if sstart <= value <= sstart + length:
            return dstart + value - sstart
    return value

locations = []
for value in seeds:
    for map in maps:
        value = next(value, map)
    locations.append(value)

print(min(locations))

# 2
minloc = 999999999999999999999

for i in range(0, len(seeds), 2):
    start, length = seeds[i], seeds[i+1]
    for value in range(start, start+length):
        for map in maps:
            value = next(value, map)
        if value < minloc:
            minloc = value

print(minloc)
