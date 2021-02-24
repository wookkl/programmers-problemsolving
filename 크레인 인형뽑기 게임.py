def solution(board, moves):
    answer = 0
    machine = [[] for _ in range(len(board))]
    stack = []
    while board:
        for i, v in enumerate(board.pop()):
            if v:
                machine[i].append(v)
    for i in moves:
        i -= 1
        if machine[i]:
            stack.append(machine[i].pop())
            if len(stack) > 1 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
    return answer
