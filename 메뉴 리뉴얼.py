from itertools import combinations


def solution(orders, course):
    answer = []

    for c in course:
        candidate_courses = list()
        for order in orders:
            candidate_courses.extend(
                list(combinations(sorted(list(order)), c)))
        candidate_courses_dict = {}
        for candidate_course in candidate_courses:
            candidate_course = "".join(list(candidate_course))
            try:
                candidate_courses_dict[candidate_course] += 1
            except:
                candidate_courses_dict[candidate_course] = 1
        if candidate_courses_dict.values():
            max_ordered_count = max(candidate_courses_dict.values())
            if max_ordered_count > 1:
                answer.extend([key for key in candidate_courses_dict.keys(
                ) if candidate_courses_dict[key] == max_ordered_count])

    return sorted(answer)
