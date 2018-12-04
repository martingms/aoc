#!/usr/bin/env python3
from collections import defaultdict, namedtuple
from datetime import datetime
from functools import reduce

# Input data
BEGINS = 0
ASLEEP = 1
WAKES = 2
LogLine = namedtuple('LogLine', ['ts', 'guard_id', 'event'])

def parse(inp):
    for line in inp:
        ts = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
        guard_id = None
        event = None
        if line[19:].startswith('Guard'):
            guard_id = int(line[26:].split(' ')[0])
            event = BEGINS
        elif line[19:].startswith('falls'):
            event = ASLEEP
        elif line[19:].startswith('wakes'):
            event = WAKES

        assert event is not None

        yield LogLine(ts, guard_id, event)

def coalesce(log):
    def reducer(acc, el):
        if el.event == BEGINS:
            return (el.guard_id, acc[1])

        acc[1].append(LogLine(el.ts, acc[0], el.event))
        return acc

    return reduce(reducer, log, (None, []))[1]

inp = open('day4.input').read().strip().split('\n')
log = coalesce(sorted(parse(inp), key=lambda l: l.ts))

assert len(log) % 2 == 0

sleep_time = defaultdict(lambda: defaultdict(int))
for i in range(0, len(log), 2):
    assert log[i].ts < log[i+1].ts
    assert log[i].guard_id == log[i+1].guard_id

    for m in range(log[i].ts.minute, log[i+1].ts.minute):
        sleep_time[log[i].guard_id][m] += 1

# 1

chosen = max(sleep_time.items(), key=lambda i: sum(i[1].values()))
print(chosen[0] * max(chosen[1].items(), key=lambda m: m[1])[0])

# 2

minutes = (
    (m, max(
        ((gid, times[m]) for gid, times in sleep_time.items()),
        key=lambda t: t[1],
    )) for m in range(0, 60)
)

chosen = max(minutes, key=lambda i: i[1][1])
print(chosen[0] *  chosen[1][0])
