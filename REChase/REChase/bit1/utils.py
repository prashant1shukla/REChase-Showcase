import random


def solve_bit1(x):
    binary = bin(int(x))[2:].zfill(8)
    binary = binary[(len(binary) - 8):]
    binary = binary[::-1]
    binary = bin(int(binary, 2) + 1)[2:].zfill(8)
    binary = binary[(len(binary) - 8):]
    binary = binary[::-1]
    return str(int(binary, 2))


def custom_rand():
    exclude = [84, 212, 73]
    x = random.choice([i for i in range(255) if i not in exclude])
    return x
