import sys


def read(func=int):
    return func(sys.stdin.readline().strip())

def readList(func=int):
    return list(map(func, sys.stdin.readline().strip().split()))


t = read()
for _ in range(t):
    players, snakes_or_ladders, rolls = readList()
    positions = [1] * players
    snakes_or_ladders_m = {}
    for _ in range(snakes_or_ladders):
        a, b = readList()
        snakes_or_ladders_m[a] = b

    do = True
    for i in range(rolls):
        if do:
            positions[i % players] += read()
            positions[i % players] = min(100, positions[i % players])
            positions[i % players] = snakes_or_ladders_m.get(
                positions[i % players], positions[i % players])
            if positions[i % players] == 100:
                do = False
        else:
            read()


    for i in range(players):
        print(f'Position of player {i + 1} is {positions[i]}.')
