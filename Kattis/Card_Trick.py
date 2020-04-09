import sys

t = int(sys.stdin.readline())


def top_to_bottom(indexes_tmp, cards_tmp):
    if len(indexes_tmp) == 0:
        return cards_tmp
    for _ in range(len(cards_tmp) - len(indexes_tmp) + 1):
        indexes_tmp = indexes_tmp[1:] + indexes_tmp[:1]
    cards_tmp[indexes_tmp.pop(0)] = len(cards_tmp) - len(indexes_tmp) + 1
    return top_to_bottom(indexes_tmp, cards_tmp)


for _ in range(t):
    n = int(sys.stdin.readline())
    indexes = [i for i in range(n)]
    cards = [0] * n
    order = top_to_bottom(indexes, cards)
    print(' '.join([str(card) for card in order]))
