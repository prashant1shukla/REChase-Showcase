def solve(x, y):
    x = str(x)
    y = str(y)
    key = 0
    chase = 0
    for i in range(0, 5):
        if x[i] == y[i]:
            key = key + 1
    for i in range(0, 5):
        for j in range(0, 5):
            if i != j and x[i] == y[j]:
                chase = chase + 1
    string = str(key) + " Keys and " + str(chase) + " Chase"
    return string


def invalid_input(x):
    if len(x) != 5 or not x.isdigit():
        return 1
    return 0
