inp = open("day2.input").read().strip().split("\n")

# 1
bag = {"red": 12, "green": 13, "blue": 14}
def game1(reveals):
    for reveal in reveals:
        for rc in (b.strip() for b in reveal.strip().split(",")):
            num, color = rc.split(" ")
            if int(num) > bag[color]:
                return False
    return True

s1 = 0
for line in inp:
    meta, cubes = line.split(":")
    id = int(meta.split(" ")[1])
    if game1(cubes.split(";")):
        s1 += id

print(s1)

# 2
from collections import defaultdict
from functools import reduce

def game2(reveals):
    max_bag = defaultdict(lambda: 0)
    for reveal in reveals:
        for rc in (b.strip() for b in reveal.strip().split(",")):
            num, color = rc.split(" ")
            num = int(num)
            if num > max_bag[color]:
                max_bag[color] = num

    return reduce(lambda a, b: a*b, max_bag.values(), 1)

s2 = 0
for line in inp:
    meta, cubes = line.split(":")
    id = int(meta.split(" ")[1])
    s2 += game2(cubes.split(";"))

print(s2)
