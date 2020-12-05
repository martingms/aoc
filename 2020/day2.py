from collections import Counter

inp = open('day2.input').read().strip().split('\n')

valid1 = 0
valid2 = 0
for line in inp:
    rule, pw = line.split(": ")
    range_, c = rule.split(" ")
    start, end = [int(x) for x in range_.split("-")]
    if start <= Counter(pw)[c] <= end:
        valid1 += 1

    start -= 1
    end -= 1
    if (len(pw) > start and pw[start] == c) ^ (len(pw) > end and pw[end] == c):
        valid2 += 1

print(valid1)
print(valid2)
