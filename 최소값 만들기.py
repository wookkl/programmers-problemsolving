def solution(A.sort(),B):
    A
    B.sort(reverse=True)
    s=0
    for i in range(len(A)):
        s+=A[i]*B[i] 
    return s