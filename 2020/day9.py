from itertools import permutations

nums = [int(n) for n in open('day9.input').read().strip().split('\n')]

def first_invalid(nums):
    for i in range(25, len(nums)):
        if not any(sum(p) == nums[i] for p in permutations(nums[i-25:i], 2)):
            return nums[i]

invalid = first_invalid(nums)
print(invalid)

def weakness(nums, invalid):
    for i in range(len(nums)):
        for j in range(i+2, len(nums)):
            s = sum(nums[i:j])
            if s == invalid:
                return min(nums[i:j]) + max(nums[i:j])
            if s > invalid:
                break

print(weakness(nums, invalid))
