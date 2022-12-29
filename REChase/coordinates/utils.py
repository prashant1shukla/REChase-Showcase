query = """Clue : <a href="https://www.worldatlas.com/flags/cayman-islands">It's all about joining the unique numbers 
in the universe</a> """


def solve(ans):
    lst = ['boiling', 'point', 'water']
    for i in lst:
        if i not in ans:
            return 0
    return 1
