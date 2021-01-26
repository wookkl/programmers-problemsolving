def break_rocks(rocks, offset):
    break_count = 0
    prev_rock = 0

    for i in range(1, len(rocks)):
        if rocks[i] - prev_rock < offset:
            break_count += 1
        else:
            prev_rock = rocks[i]

    return break_count


def solution(distance, rocks, n):
    rocks.sort()
    left, right = 1, distance

    while left + 1 < right:
        mid = (left + right) // 2
        res = break_rocks([0]+rocks, mid)

        if res > n:
            right = mid
        else:
            left = mid

    return left
