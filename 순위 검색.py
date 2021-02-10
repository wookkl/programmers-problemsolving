from itertools import combinations


def make_combi():
    info_dict = dict()
    lang = ["", "cpp", "java", "python"]
    group = ["", "backend", "frontend"]
    career = ["", "junior", "senior"]
    food = ["", "chicken", "pizza"]

    for l in lang:
        for g in group:
            for c in career:
                for f in food:
                    a = [x for x in [l, g, c, f] if x != ""]
                    info_dict[" ".join(a)] = []

    return info_dict


def solution(info, query):
    answer = []
    info_dict = make_combi()

    for i in info:
        l = i.split(" ")
        _info, score = l[:4], l[-1]
        for n in range(5):
            for comb in list(combinations(_info, n)):
                info_dict[" ".join(list(comb))].append(score)

    for key in info_dict.keys():
        info_dict[key] = sorted(list(map(int, info_dict[key])))

    for q in query:
        q = [x for x in q.split(" ") if x != "and" and x != "-"]
        goal = int(q.pop())
        scores = info_dict[" ".join(q)]
        start, end = 0, len(scores)

        while start < end:
            mid = (start + end) // 2

            if scores[mid] >= goal:
                end = mid
            else:
                start = mid + 1

        answer.append(len(scores)-start)

    return answer
