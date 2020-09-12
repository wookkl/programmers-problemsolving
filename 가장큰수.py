def solution(numbers):
    numbers = [list(str(x)) for x in numbers]
    numbers = sorted(numbers, key = lambda  x : (x[0], x[1%len(x)], x[2%len(x)], x[3%len(x)]),reverse=True)    
    answer = ''.join([''.join(x) for x in numbers])
    if set("0") == set(answer):
        return '0'
    else:
        return answer