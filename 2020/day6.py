groups = open('day6.input').read().strip().split('\n\n')
set_groups = [[set(p) for p in g.split("\n")] for g in groups]
print(sum(len(set.union(*sg)) for sg in set_groups))
print(sum(len(set.intersection(*sg)) for sg in set_groups))
