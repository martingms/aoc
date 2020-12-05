import re

inp = open('day4.input').read().strip().split('\n\n')

def hgt_validator(h):
    value, unit = int(h[:-2]), h[-2:]
    if unit == "cm":
        return 150 <= value <= 193
    if unit == "in":
        return 59 <= value <= 76
    return False

validators = {
    "byr": lambda y: 1920 <= int(y) <= 2002,
    "iyr": lambda y: 2010 <= int(y) <= 2020,
    "eyr": lambda y: 2020 <= int(y) <= 2030,
    "hgt": lambda h: hgt_validator,
    "hcl": lambda c: re.match("#[0-9a-f]{6}", c),
    "ecl": lambda c: c in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda i: re.match("\d{9}", i),
}

npresent, nvalid = 0, 0
for entry in inp:
    fields = {}
    for field in entry.replace("\n", " ").split(" "):
        tag, value = field.split(":")
        fields[tag] = value
    all_present = all(tag in fields for tag in validators.keys())
    if all_present:
        npresent += 1
    try:
        all_valid = all(validators[tag](value) for tag, value in fields.items() if tag in validators)
    except Exception:
        continue
    if all_present and all_valid:
        nvalid += 1

print(npresent)
print(nvalid)
