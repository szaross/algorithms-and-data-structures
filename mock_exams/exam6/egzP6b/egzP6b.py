from egzP6btesty import runtests


def jump(M):
    moves = {
        "UL": (-2, -1),
        "UR": (-2, 1),
        "RU": (-1, 2),
        "RD": (1, 2),
        "DR": (2, 1),
        "DL": (2, -1),
        "LD": (1, -2),
        "LU": (-1, -2),
    }
    count = {}
    count[(0, 0)] = 1

    x, y = 0, 0
    for move in M:
        dx, dy = moves[move]
        x, y = x + dx, y + dy
        if (x, y) in count:
            count[(x, y)] += 1
        else:
            count[(x, y)] = 1

    odds = 0
    for key, value in count.items():
        if value % 2:
            odds += 1

    return odds


runtests(jump, all_tests=True)
