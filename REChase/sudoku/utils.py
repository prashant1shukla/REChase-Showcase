n = 7
symbols = {
    '1d': 1,
    'a3': -1,
    '2b': 1,
    '2e': 1,
    'b1': -1,
    'b2': 1,
    'b4': 1,
    '3f': -1,
    'c3': 1,
    'c5': -1,
    'c6': 1,
    '4a': -1,
    '4b': -1,
    '4d': -1,
    '4e': -1,
    'd2': -1,
    '5a': 1,
    '5d': 1,
    '5f': -1,
    'e5': 1,
    '6b': -1,
    '6d': -1,
    '6f': 1,
    'f1': -1,
    'f3': 1,
    '7a': 1,
    '7d': 1,
    '7e': 1,

}

prefilled = {
    '11': 5,
    '16': 6,
    '47': 1,
    '77': 5

}


def rowChecker(arr):
    for i in range(n):
        temp = sorted(arr[i])
        for j in range(n):
            if temp[j] != j + 1:
                return 0
    return 1


def colChecker(arr):
    for j in range(n):
        temp = [arr[i][j] for i in range(n)]
        temp.sort()
        for i in range(n):
            if temp[i] != i + 1:
                return 0
    return 1


def getIndices(s):
    r, c = s[0], s[1]
    if r.isalpha():
        r = ord(r) - ord('a')
        c = int(c) - 1
        direction = 1  # down
    else:
        r = int(r) - 1
        c = ord(c) - ord('a')
        direction = 0  # side
    return r, c, direction


def masterChecker(arr):
    if (not colChecker(arr)) or (not rowChecker(arr)):
        return 0

    for key, val in symbols.items():
        r, c, direction = getIndices(key)
        if direction == 0:
            if arr[r][c] + val != arr[r][c + 1]:
                return 0
        else:
            if arr[r][c] + val != arr[r + 1][c]:
                return 0
    return 1
