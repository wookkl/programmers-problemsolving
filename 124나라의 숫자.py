def solution(n):
    answer =[]
    l=['1','2','4']
    while n: 
        answer.append(l[(n-1)%3])
        n=(n-1)//3
    return ''.join(answer[::-1])