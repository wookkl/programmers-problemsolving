def get_milli_seconds(t):
    h, m, s = map(float, t.split(":"))
    return int(1000 * (h * 3600 + m * 60 + s))


def solution(lines):
    answer = 0
    times = []
    for idx, line in enumerate(lines):
        _, s, t = line.split(" ")
        s = get_milli_seconds(s)
        t = int(float(t.replace('s', ''))*1000)
        start = s - t + 1
        end = s
        lines[idx] = [start, end]
        times.extend([start, end])
    times = sorted(list(set(times)))

    for t in times:
        c = 0
        for s, e in lines:
            if t - 999 <= e and s <= t:
                c += 1
        answer = max(c, answer)
    return answer
