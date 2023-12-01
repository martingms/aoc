inp = open("day1.input").read().strip().split("\n")

# 1
nextdigit = lambda l: next(int(c) for c in l if c.isdigit())
print(sum(nextdigit(l)*10 + nextdigit(reversed(l)) for l in inp))

# 2 
words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def digits(line):
    for start in range(len(line)):
        if line[start].isdigit():
            yield int(line[start])
        else:
            for i, word in enumerate(words):
                if line[start:].startswith(word):
                    yield i+1

print(sum(ds[0]*10 + ds[-1] for ds in (list(digits(l)) for l in inp)))
