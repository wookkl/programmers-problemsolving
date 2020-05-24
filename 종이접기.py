def rev(l):
    for i in range(len(l)):
        if l[i] == 0 :
            l[i]=1
        else:
            l[i]=0
    l.reverse()
    return l
def solution(n):
    answer = [0]
    for i in range(n-1):
        mid=len(answer)//2
        answer = answer+[answer[len(answer)//2]]+rev(answer)
    return answer
