def solution(n):
    answer=1
    l=[1]
    while l[-1] < n//2+2:
        if sum(l)<n:
            l.append(l[-1]+1)
        elif sum(l)>n:
            l.pop(0)
        else:
            l.pop(0)
            l.append(l[-1]+1)
            answer+=1
    return answer
