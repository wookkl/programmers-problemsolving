def solution(n):
    a,b=0,1
    for i in range(n):
        tmp=b
        b=(a+b)%1234567
        a=tmp
    return b