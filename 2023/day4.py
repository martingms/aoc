inp = open("day4.input").read().strip().split("\n")

def nums(s): return {int(n) for n in s.split()}
def matching(card):
    winning, our = card.split(": ")[1].split("|")
    return len(nums(winning).intersection(nums(our)))

# 1
print(sum(int(2**(matching(line)-1)) for line in inp))

# 2
copies = [1] * len(inp)
for idx, card in enumerate(inp):
    hits = matching(card)
    for i in range(hits):
        copies[idx + i + 1] += copies[idx]

print(sum(copies))
