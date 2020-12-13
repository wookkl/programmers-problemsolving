from itertools import permutations


def available(weak, friends):
    for _ in range(len(friends)):
        dist = friends.pop()
        idx = 0
        while weak:
            if len(weak) != idx and dist >= weak[idx] - weak[0]:
                idx += 1
            else:
                idx -= 1
                break
        weak.reverse()
        for _ in range(idx + 1):
            if weak:
                weak.pop()
        weak.reverse()
    if len(weak) == 0:
        return True
    else:
        False


def solution(n, weak, dist):
    _len = len(weak)
    for i in range(len(weak)):
        weak.append(weak[i] + n)

    for num in range(len(dist)):
        for i in permutations(dist, num + 1):
            for j in range(_len):
                new_weak = weak[j : j + _len]
                if available(new_weak.copy(), list(i)):
                    return len(i)
    return -1
