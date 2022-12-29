from math import factorial as fact
import random

names = [
    'CORDIAL', 'PELTER', 'TWAIN', 'FARMER', 'REVOLT', 'FAMINE', 'CLOUD', 'MUSIC', 'BEANS', 'STRONG', 'MOSQUITO',
    'DINOSAUR', 'CRAYON',
    'TURTLE', 'WIZARD', 'PIRATE', 'BATTERY', 'PENGUIN', 'OCTOPUS', 'NATURAL', 'MARATHON', 'BLENDER', 'POISON', 'GUITAR',
    'CONTRAST', 'MODERATE', 'TRIANGLE', 'UMBRELLA'
]


# Find number of remaining smaller
def smaller_char(st, ind):
    count = 0
    i = ind + 1
    while i < len(st):
        if st[i] < st[ind]:
            count += 1
        i += 1
    return count


# Find factorial of remaining duplicates
def duplicates(st):
    new_st = ''
    for char in st:
        if char not in new_st:
            new_st += char
    num = len(st) - len(new_st)
    return 2 ** num


def word_rank(word):
    rank = 1
    for i in range(len(word)):
        dup = duplicates(word[i:])
        small = smaller_char(word, i)
        rank += (small * fact(len(word) - i - 1)) / dup
    return int(rank)


def solve(x):
    return word_rank(x.upper())


def compare(x, y):
    a = ''.join(sorted(x.upper()))
    b = ''.join(sorted(y.upper()))
    if str(a) == str(b):
        return 1
    else:
        return 0


def getname():
    name = names[random.randint(0, len(names) - 1)]
    ans = solve(name)
    query = name + " " + str(ans)
    return query


def getquery(que, x):
    string = "If {} scores {} who will be scoring {}.\nRemember the one who will be scoring will have the same " \
             "alphabets in its name but in some other order. \nIf you found it just tell me and I will take you  " \
             "closer to the treasure. ".format(que.split()[0], que.split()[1], x)
    return string
