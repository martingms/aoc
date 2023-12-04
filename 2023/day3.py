inp = open("day3.input").read().strip().split("\n")

def parsenum(line):
    digits = 0
    acc = 0
    for i, c in enumerate(line):
        if not c.isdigit():
            break
        digits += 1
        acc *= 10
        acc += int(c)
    return digits, acc

# 1

points = set()
for y, line in enumerate(inp):
    for x, char in enumerate(line):
        if char != "." and not char.isdigit():
            for xp in [x-1, x, x+1]:
                for yp in [y-1, y, y+1]:
                   points.add((xp, yp))

s = 0
for y, line in enumerate(inp):
    x = 0
    while x < len(line):
        digits, num = parsenum(line[x:])
        if num and any((xp, y) in points for xp in range(x, x+digits)):
            s += num
            x += digits
        else:
            x += 1

print(s)

# 2

gears = {}
for y, line in enumerate(inp):
    for x, char in enumerate(line):
        if char == "*":
            gears[(x, y)] = []

def maybeappend(x, digits, y, num):
    for yp in [y-1, y, y+1]:
        for xp in range(x-1, x+digits+1):
            if (xp, yp) in gears:
                gears[(xp, yp)].append(num)
                return

s = 0
for y, line in enumerate(inp):
    x = 0
    while x < len(line):
        digits, num = parsenum(line[x:])
        if num:
            maybeappend(x, digits, y, num)
            x += digits
        else:
            x += 1

s = 0
for nums in gears.values():
    if len(nums) == 2:
        s += nums[0] * nums[1]

print(s)
