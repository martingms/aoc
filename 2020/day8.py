code = [l.split(" ") for l in open('day8.input').read().strip().split('\n')]
code = [[inst, int(v)] for (inst, v) in code]

def eval(code):
    addr, acc = 0, 0
    seen = set()
    while True:
        if addr not in range(0, len(code)):
            return acc, True
        if addr in seen:
            return acc, False
        seen.add(addr)

        instr, val = code[addr]
        addr += val if instr == "jmp" else 1
        acc += val if instr == "acc" else 0

print(eval(code)[0])

for line in code:
    if line[0] == "nop":
        line[0] = "jmp"
        acc, halted = eval(code)
        if halted:
            print(acc)
            break
        line[0] = "nop"
    elif line[0] == "jmp":
        line[0] = "nop"
        acc, halted = eval(code)
        if halted:
            print(acc)
            break
        line[0] = "jmp"
