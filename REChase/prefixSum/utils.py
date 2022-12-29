import random

NAMES = ['INCEPTION']
SAMPLE_NAMES = ['INCEPTION']


def solve(s: str):
    n = len(s)
    if n <= 2:
        return None
    l1 = [ord(i) - 64 for i in s]
    for i in range(1, n):
        l1[i] += l1[i - 1]
    return ''.join(map(str, l1))


def func(sample=True):
    if sample:
        name = random.choice(SAMPLE_NAMES)
    else:
        name = random.choice(NAMES)
    ans = solve(name)
    return name, ans
