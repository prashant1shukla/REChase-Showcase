import random

TURBAN_NUMBERS = [1, 5, 6, 7, 9, 11]
NON_TN = [i for i in range(1, 1000) if i not in TURBAN_NUMBERS]


def solve(x):
    ans = ''.join(map(lambda num: 'Y' if num in TURBAN_NUMBERS else 'N', x))
    return ans


def makeSequence():
    turbans = random.sample(TURBAN_NUMBERS, random.randint(2, 3))
    non_turbans = random.sample(NON_TN, 7 - len(turbans))
    temp = turbans + non_turbans
    random.shuffle(temp)
    return temp
