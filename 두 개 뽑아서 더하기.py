def solution(numbers):
    return sorted(list(set(numbers[x]+numbers[y] for x in range(len(numbers)) for y in range(len(numbers)) if x != y)))
