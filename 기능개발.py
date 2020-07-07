def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()
    while progresses: 
        c=0
        for i in range(len(progresses)-1,-1,-1): 
            progresses[i]+=speeds[i]
        if progresses[-1] >=100:
            for i in range(len(progresses)-1,-1,-1): 
                if progresses[i]>=100:
                    progresses.pop()
                    speeds.pop()
                    c+=1
        if c:answer.append(c)
    return answer
print(solution([93,30,55],[1,30,5]))